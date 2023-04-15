#!/bin/bash
#SBATCH --job-name=kk_dicts
##SBATCH --partition=gpu
##SBATCH --gres=gpu:1
#SBATCH --error=Job.%J.err
#SBATCH --output=Job.%J.out
#SBATCH --time=96:00:00



cd $SLURM_SUBMIT_DIR

module load cdac/DL_conda_3.7/3.7



python3 scoring_dict_r.py

