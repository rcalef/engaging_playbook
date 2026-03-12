#! /bin/bash
set -eux

srun "$@" -p pi_manoli -c 12 --mem=120GB -t 4:0:0 --gres=gpu:1 --pty bash 
