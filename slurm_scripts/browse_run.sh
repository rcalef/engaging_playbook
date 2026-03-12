#! /bin/bash

srun "$@" -p ou_bcs_low -c 8 --mem=10GB -t 12:0:0 --pty bash 
