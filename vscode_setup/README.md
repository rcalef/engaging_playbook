This directory contains a script and example SSH config for how I connect the IDE running on my laptop to a compute node on Engaging

Prerequisites:
- Ability to ssh into the Engaging login node using SSH keys

`example_ssh_config` contains an example SSH config based on my config. Something like
this should be at `~/.ssh/config` on your local machine (e.g. your laptop).

This block:
```
Host eng
    User YOUR_NAME_HERE
    HostName orcd-login003.mit.edu
    ServerAliveInterval 60
    ServerAliveCountMax 30
```
defines the alias for the Engaging login node, allowing you to login like:
```
ssh eng
```
followed by two-factor authentication with Duo.

This block:
```
Host engnode
    HostName node2803
    ProxyJump eng
    User YOUR_NAME_HERE
    PreferredAuthentications publickey
    PasswordAuthentication no
    # Replace with the path to your private key
    IdentityFile /path/to/home/.ssh/id_rsa
    ServerAliveInterval 60
    ServerAliveCountMax 30
```
is the alias for the compute node that your interactive job will be running on, and
ultimately where you will be running your IDE.

The workflow looks like this:
1. ssh into Engaging login node (`ssh eng`)
2. allocate an interactive job (`browse_run.sh`, if you're using the scripts from `../slurm_scripts` and they're in your path)
3.  note the node you've been allocated (this should either be part of your command prompt, or you can check under NODELIST in `squeue --me`)
4. edit `~/.ssh/config` on your local machine so that the `HostName` line in the `engnode` block lists the node you've been allocated
5. reload your IDE and tell it to connect to `engnode`

The script `,ssh_config_update.py` is just to simplify step 4 above. It takes two arguments: the target host entry (e.g. `engnode`) and the new hostname (e.g. `node2803`) and updates the SSH config file, e.g.:
```
,ssh_config_update.py engnode node3904
```
The leading comma is just to make it easy to tab-complete the script name, so can be removed if you don't like it.