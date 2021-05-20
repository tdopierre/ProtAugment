#!/usr/bin/env bash
#SBATCH -n 1
#SBATCH -p GPU
#SBATCH -J run_language_modeling
#SBATCH -o run_language_modeling.log
#SBATCH --gres=gpu:1
#SBATCH --exclude=calcul-gpu-lahc-2
source .venv/bin/activate
echo "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}"
echo "GPU Devices:"
nvidia-smi


for dataset in BANKING77 HWU64 Liu OOS; do
    model_type=bert
    model_name=bert-base-cased

    block_size=64

    output_dir=transformer_models/${dataset}/fine-tuned

    python language_modeling/run_language_modeling.py \
        --model_name_or_path ${model_name} \
        --output_dir ${output_dir} \
        --mlm \
        --do_train \
        --train_data_file data/${dataset}/mlm/mlm-train.txt  \
        --do_eval \
        --eval_data_file data/${dataset}/mlm/mlm-test.txt \
        --overwrite_output_dir \
        --logging_steps=1000 \
        --line_by_line \
        --logging_dir ${output_dir} \
        --block_size ${block_size} \
        --save_steps=1000 \
        --num_train_epochs 5 \
        --save_total_limit 5 \
        --seed 42
done
