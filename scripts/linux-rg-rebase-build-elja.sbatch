#!/bin/bash
#SBATCH --job-name=linux-rg-718
#SBATCH --account=chem-ui
#SBATCH --partition=64cpu_256mem
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=04:00:00

set -euo pipefail

if [[ -f /opt/ohpc/admin/lmod/lmod/init/bash ]]; then
  # shellcheck disable=SC1091
  source /opt/ohpc/admin/lmod/lmod/init/bash
fi
export MODULEPATH=${MODULEPATH:-/opt/ohpc/pub/modulefiles}
module load gnu12

repo=${LINUX_RG_REPO:?set LINUX_RG_REPO}
tree=${LINUX_RG_REBASE_TREE:?set LINUX_RG_REBASE_TREE}

echo "host=$(hostname) job=${SLURM_JOB_ID:-none} gcc=$(gcc -dumpfullversion 2>/dev/null || gcc -dumpversion)"
date -Is
bash "$repo/scripts/linux-rg-rebase-build" "$tree" rgam5terra
date -Is
