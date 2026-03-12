This directory contains a sample of SLURM `srun` scripts for running
interactive compute jobs with various amounts of resources. These are all
interactive jobs, i.e. they open a bash shell in the allocated node, but
these parameters can also be translated into sbatch headers for asynchronous
jobs. The scripts:
- `browse_run.sh` - good for running your IDE and light data exploration (8 CPU cores and 10GB of RAM)
- `cpu_run.sh` - good for larger CPU-driven jobs like large data wrangling (32 CPU cores and 96GB of RAM)
- `gpu_run.sh` - single GPU job for any GPU-driven compute (1 A100 (80 GB of VRAM), 12 CPU cores, 120 GB of RAM)
    - this script uses our lab partition
- `mit_h200_run.sh` - single H200 job for GPU-driven compute with larger VRAM needs (1 H200 (141 GB of VRAM), 15 CPU cores, 240 GB of RAM)


To use these scripts, either add this path directly to your `PATH` environment variable in your `.bashrc`, or copy them to some other directory in your `PATH` (e.g. `~/bin`).