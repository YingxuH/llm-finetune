#! /usr/bin/env bash

set -ex

PRE_SEQ_LEN=128
LR=2e-2
NUM_GPUS=2
MAX_SEQ_LEN=2048
DEV_BATCH_SIZE=1
GRAD_ACCUMULARION_STEPS=16
MAX_STEP=1000
SAVE_INTERVAL=500

DATESTR=`date +%Y%m%d-%H%M%S`
RUN_NAME=conversations_pt

BASE_MODEL_PATH=THUDM/chatglm3-6b
DATASET_PATH=formatted_data/conversations.jsonl
OUTPUT_DIR=output/${RUN_NAME}-${DATESTR}-${PRE_SEQ_LEN}

mkdir -p $OUTPUT_DIR

torchrun --standalone --nnodes=1 --nproc_per_node=1 finetune.py \
    --train_format multi-turn \
    --train_file $DATASET_PATH \
    --max_seq_length 1024 \
    --preprocessing_num_workers 1 \
    --model_name_or_path $BASE_MODEL_PATH \
    --output_dir $OUTPUT_DIR \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --num_train_epochs 2 \
    --logging_steps 1 \
    --save_steps 100 \
    --fp16 True \
    --learning_rate 2e-2 \
    --optim adamw_torch \
    --lr_scheduler_type cosine \
    --warmup_ratio 0.03 \
    --pre_seq_len $PRE_SEQ_LEN 2>&1 | tee ${OUTPUT_DIR}/train.log
