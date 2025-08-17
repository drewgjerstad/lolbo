#!/bin/bash -l

# SETUP RESOURCE
#SBATCH --time=10:00:00
#SBATCH --ntasks=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=gjers043@umn.edu
#SBATCH -p v100
#SBATCH --gres=gpu:v100:1
#SBATCH --output=output_pdop.txt

conda activate lolbo-env