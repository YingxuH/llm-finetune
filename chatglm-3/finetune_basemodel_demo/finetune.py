#!/usr/bin/env python
# coding=utf-8
# Copyright 2021 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Fine-tuning the library models for sequence to sequence.
"""
# You can also adapt this script on your own sequence to sequence task. Pointers for this are left as comments.
# Adapted from


import logging
import os
import sys
import json
import random
import transformers
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    DataCollatorForSeq2Seq,
    HfArgumentParser,
    Seq2SeqTrainingArguments,
    set_seed,
)
from trainer import LoRATrainer
from arguments import ModelArguments, DataTrainingArguments
from peft import get_peft_model, LoraConfig, TaskType
from preprocess_utils import InputOutputDataset, MultiTurnDataset
import torch


device = "cuda"
logger = logging.getLogger(__name__)


def prepare_precision_for_mixed_training(model, model_args):
    if model_args.model_dtype != 32:
        for param in model.parameters():
            if param.requires_grad:
                param.data = param.data.to(torch.float32)
    return model

def prepare_dataset(tokenizer, data_args):
    with open(data_args.train_file, "r", encoding="utf-8") as f:
        if data_args.train_file.endswith(".json"):
            train_data = json.load(f)
        elif data_args.train_file.endswith(".jsonl"):
            train_data = [json.loads(line) for line in f]

    if data_args.validation_file:
        with open(data_args.validation_file, "r", encoding="utf-8") as f:
            if data_args.validation_file.endswith(".json"):
                valid_data = json.load(f)
            elif data_args.validation_file.endswith(".jsonl"):
                valid_data = [json.loads(line) for line in f]
    elif data_args.validation_rate > 0:
        cut = int(len(train_data) * data_args.validation_rate + 1)
        random.shuffle(train_data)
        valid_data = train_data[:cut]
        train_data = train_data[cut:]
    else:
        valid_data = None
        
    train_dataset = MultiTurnDataset(
        train_data,
        tokenizer,
        data_args.max_source_length
    )   
    
    if valid_data:
        valid_dataset = MultiTurnDataset(
            valid_data,
            tokenizer,
            data_args.max_source_length
        )
    else:
        valid_dataset = None

    return train_dataset, valid_dataset

def main():
    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, Seq2SeqTrainingArguments))
    if len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        model_args, data_args, training_args = parser.parse_json_file(json_file=os.path.abspath(sys.argv[1]))
    else:
        model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    training_args.ddp_find_unused_parameters = False
    training_args.save_safetensors = False

    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    if training_args.should_log:
        transformers.utils.logging.set_verbosity_info()

    log_level = training_args.get_process_log_level()
    logger.setLevel(log_level)
    transformers.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.enable_default_handler()
    transformers.utils.logging.enable_explicit_format()

    # Log on each process the small summary:
    logger.warning(
        f"Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
        + f"distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
    )
    logger.info(f"Training/evaluation parameters {training_args}")
    set_seed(training_args.seed)

    config = AutoConfig.from_pretrained(model_args.model_name_or_path, trust_remote_code=True)
    config.use_cache = False

    tokenizer = AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        trust_remote_code=True
        )
    
    model_dtype = torch.float32 if model_args.model_dtype == 32 else torch.float16

    model = AutoModelForCausalLM.from_pretrained(
        model_args.model_name_or_path, 
        torch_dtype=model_dtype,
        trust_remote_code=True
        ).cuda()

    train_dataset, valid_dataset = prepare_dataset(tokenizer, data_args)
    print(f"Train dataset size: {len(train_dataset)}")

    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        inference_mode=False,
        r=model_args.lora_rank,
        target_modules=model_args.lora_trainable.split(","),
        lora_alpha=model_args.lora_alpha,
        lora_dropout=model_args.lora_dropout,
    )

    model = get_peft_model(model, peft_config).to(device)

    if training_args.fp16 or training_args.bf16:
        model = prepare_precision_for_mixed_training(model, model_args)
    
    model.config.use_cache = False

    data_collator = DataCollatorForSeq2Seq(
        tokenizer,
        model=model,
        label_pad_token_id=-100,
        pad_to_multiple_of=8,
        padding=True
    )

    # Initialize our Trainer
    trainer = LoRATrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=valid_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )
    

    checkpoint = None
    if training_args.resume_from_checkpoint is not None:
        checkpoint = training_args.resume_from_checkpoint

    model.gradient_checkpointing_enable()
    model.enable_input_require_grads()
    
    with torch.autocast(device):
        trainer.train(resume_from_checkpoint=checkpoint)
    trainer.save_model()  # Saves the tokenizer too for easy upload
    # trainer.save_state()


if __name__ == "__main__":
    main()
