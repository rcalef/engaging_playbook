# Overview

This is an example Python project demonstrating how to do a few things:
- Specify dependencies and setting up a project-specific virtual environment using `uv`
- Demonstrate how to set up commonly used dependencies like PyTorch and FlashAttention


## FlashAttention install
1. `module load cuda/13.1.0` - this is needed to make sure the flash attention install can access the CUDA libraries it needs to build from source. After running this command, `module list` should show `gcc/12.2.0` and `cuda/13.1.0` amongst any other modules you've loaded 
