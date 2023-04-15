#!/bin/bash
#SBATCH --job-name=kk_plot
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --error=Job.%J.err
#SBATCH --output=Job.%J.out
#SBATCH --time=24:00:00



cd $SLURM_SUBMIT_DIR

module load cdac/DL_conda_3.7/3.7



python3 get_nbrslen_txts.py



