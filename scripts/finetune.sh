#!/bin/bash

exp_tag="e1"
python finetune.py \
    --base_model 'decapoda-research/llama-7b-hf' \
    --data_path './data/llama_data.json' \
    --output_dir './lora-llama-med-'$exp_tag \
    --prompt_template_name 'med_template' \
    --micro_batch_size 128 \
    --batch_size 128 \
    --wandb_run_name $exp_tag