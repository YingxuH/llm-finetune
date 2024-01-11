#! /usr/bin/env bash

set -ex
export CUDA_VISIBLE_DEVICES=0,1
export PYTHONUNBUFFERED=True

RUN_NAME=text
DATASET_PATH=/opt/datasets/Alpaca-COT/.json
VALIDATION_DATASET_PATH=data/alpaca_data.jsonl
DATESTR=`date +%Y%m%d-%H%M%S`
BASE_MODEL_NAME=chatglm3-6b
BASE_MODEL_PATH=THUDM/chatglm3-6b-base
CACHE_DIR=
OUTPUT_DIR=output/${RUN_NAME}-${DATESTR}-${LR}
MASTER_PORT=$(shuf -n 1 -i 10000-65535)
mkdir -p $OUTPUT_DIR

python finetune.py \
    --train_file $DATASET_PATH \
    --valid_file $VALIDATION_DATASET_PATH \
    --model_name_or_path $BASE_MODEL_PATH \
    --preprocessing_num_workers 1 \
    --output_dir $OUTPUT_DIR \
    --lora_rank 8 \
    --lora_alpha 16 \
    --lora_dropout 0.1 \
    --max_source_length 512 \
    --max_target_length 128 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 32 \
    --eval_accumulation_steps 32 \
    --num_train_epochs 4 \
    --logging_steps 1 \
    --evaluation_strategy steps \
    --eval_steps 50 \
    --save_steps 50 \
    --model_dtype 16 \
    --fp16 True \
    --fp32 False \
    --fp16_opt_level O1 \
    --optim adamw_torch \
    --warmup_steps 100 \
    --learning_rate 2e-5 2>&1 | tee ${OUTPUT_DIR}/train.log

