#! /bin/bash
set -eux

srun "$@" -p mit_normal_gpu -c 15 --mem=240GB -t 8:0:0 --gres=gpu:h200:1 --pty bash 
