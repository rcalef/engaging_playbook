# Overview

This is an example Python project demonstrating how to do a few things:
- Specify dependencies and setting up a project-specific virtual environment using `uv`
- Demonstrate how to set up commonly used dependencies like PyTorch and FlashAttention


## FlashAttention install
FlashAttention install will build from source, requiring a decent amount of resources. I've succesfully installed using an interactive job with the following resources:
```
srun -p mit_normal -c 32 --mem=96GB -t 8:0:0 --pty bash
```
Once you're in the interactive job, follow these instructions to install:
1. `module load cuda/13.1.0` - this is needed to make sure the flash attention install can access the CUDA libraries it needs to build from source. After running this command, `module list` should show `gcc/12.2.0` and `cuda/13.1.0` amongst any other modules you've loaded 
2. `uv sync` - install other packages required for flash attention, namely `torch` and `ninja`
3. `MAX_JOBS=4 uv sync --extra flash` - install flash attention

Now you can verify the installation with:
```
source .venv/bin/activate
python -c "from flash_attn import flash_attn_qkvpacked_func, flash_attn_func; print('done')"
```
