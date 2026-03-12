#! /bin/bash

srun -p mit_normal -c 32 --mem=96GB -t 8:0:0 --pty bash
