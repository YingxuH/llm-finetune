#! /usr/bin/env bash

set -ex
export CUDA_VISIBLE_DEVICES=0
export PYTHONUNBUFFERED=True

RUN_NAME=lora_conversations
DATASET_PATH=formatted_data/conversations.jsonl
# VALIDATION_DATASET_PATH=data/alpaca_data.jsonl
DATESTR=`date +%Y%m%d-%H%M%S`
BASE_MODEL_NAME=chatglm3-6b
BASE_MODEL_PATH=THUDM/chatglm3-6b
OUTPUT_DIR=/content/drive/MyDrive/lora_results/output/${RUN_NAME}-${DATESTR}
MASTER_PORT=$(shuf -n 1 -i 10000-65535)
mkdir -p $OUTPUT_DIR

nohup python finetune.py \
    --train_format multi-turn \
    --train_file $DATASET_PATH \
    --validation_rate 0.1 \
    --model_name_or_path $BASE_MODEL_PATH \
    --preprocessing_num_workers 1 \
    --output_dir $OUTPUT_DIR \
    --lora_rank 8 \
    --lora_alpha 16 \
    --lora_dropout 0.1 \
    --lora_trainable query_key_value,embed_tokens,lm_head \
    --max_source_length 1024 \
    --max_target_length 512 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 16 \
    --eval_accumulation_steps 16 \
    --num_train_epochs 4 \
    --logging_steps 5 \
    --evaluation_strategy steps \
    --eval_steps 50 \
    --save_steps 50 \
    --model_dtype 16 \
    --fp16 True \
    --fp16_opt_level O1 \
    --optim adamw_torch \
    --lr_scheduler_type cosine \
    --warmup_ratio 0.03 \
    --learning_rate 3e-4 > ${OUTPUT_DIR}/train.log 2>&1 &

