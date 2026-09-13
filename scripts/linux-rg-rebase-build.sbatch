#!/bin/bash
#SBATCH --job-name=linux-rg-718
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=28
#SBATCH --mem=32G
#SBATCH --time=04:00:00

set -euo pipefail
repo=${LINUX_RG_REPO:?set LINUX_RG_REPO}
tree=${LINUX_RG_REBASE_TREE:?set LINUX_RG_REBASE_TREE}
echo "host=$(hostname) job=${SLURM_JOB_ID:-none} cpus=${SLURM_CPUS_PER_TASK:-$(nproc)}"
date -Is
bash "$repo/scripts/linux-rg-rebase-build" "$tree" rgam5terra
date -Is
