#!/bin/bash -l

# SETUP RESOURCE
#SBATCH --time=10:00:00
#SBATCH --ntasks=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=gjers043@umn.edu
#SBATCH -p v100
#SBATCH --gres=gpu:v100:1
#SBATCH --output=output_logp_512_2.txt

source ~/.bashrc
source /users/6/gjers043/anaconda3/etc/profile.d/conda.sh

conda activate lolbo-env
cd /users/6/gjers043/lolbo/scripts/
CUDA_VISIBLE_DEVICES=0 python3 molecule_optimization.py --seed 1234 --max_string_length 512 --task_id logp --max_n_oracle_calls 500 --bsz 1 --k 10 - run_lolbo - done