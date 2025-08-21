#!/bin/bash -l

# SETUP RESOURCE
#SBATCH --time=06:00:00
#SBATCH --ntasks=16
#SBATCH --mail-type=ALL
#SBATCH --mail-user=gjers043@umn.edu
#SBATCH -p msigpu
#SBATCH --gres=gpu:a100:1
#SBATCH --output=analysis/output/output_med2.txt

# LOL-BO PARAMETERS
GPU_DEVICES="0"
SEED=87364
TASK_ID=med2
MAX_STRING_LENGTH=400
MAX_N_ORACLE_CALLS=50000
BATCH_SIZE=10

# Locate Conda Profile and Environment
source ~/.bashrc
source /users/6/gjers043/anaconda3/etc/profile.d/conda.sh
conda activate lolbo-env

# Run LOL-BO
cd /users/6/gjers043/lolbo/scripts/
module load cuda
CUDA_VISIBLE_DEVICES=$GPU_DEVICES python3 molecule_optimization.py \
    --seed $SEED \
    --task_id $TASK_ID \
    --max_string_length $MAX_STRING_LENGTH \
    --max_n_oracle_calls $MAX_N_ORACLE_CALLS \
    --bsz $BATCH_SIZE \
    - run_lolbo - done