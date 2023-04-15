#!/bin/bash
#SBATCH --job-name=kk_decomp
##SBATCH --partition=gpu
##SBATCH --gres=gpu:1
#SBATCH --error=Decomp.%J.err
#SBATCH --output=Decomp.%J.out
#SBATCH --time=96:00:00



cd $SLURM_SUBMIT_DIR

module load cdac/DL_conda_3.7/3.7



python3 Dict_to_Decomp.py

