#!/usr/bin/env python3
import sys
import os

def update_ssh_config(target_host, new_hostname, config_path=os.path.expanduser("~/.ssh/config")):
    # Read the existing SSH config file.
    try:
        with open(config_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: SSH config file '{config_path}' not found.")
        sys.exit(1)

    updated_lines = []
    i = 0
    host_found = False

    while i < len(lines):
        line = lines[i]
        # Detect the start of a Host block
        if line.strip().startswith("Host "):
            # Split the line to get a list of host names (there might be several)
            parts = line.strip().split()[1:]
            if target_host in parts:
                host_found = True
                # Collect the entire host block
                block = [line]
                i += 1
                while i < len(lines) and not lines[i].lstrip().startswith("Host "):
                    block.append(lines[i])
                    i += 1

                # Process the block: update HostName if it exists.
                found_hostname = False
                new_block = []
                for blk_line in block:
                    # Check if the line is a HostName line (ignoring leading whitespace)
                    if blk_line.lstrip().startswith("HostName "):
                        # Preserve the original indentation.
                        indent = blk_line[:blk_line.find("HostName")]
                        new_block.append(f"{indent}HostName {new_hostname}\n")
                        found_hostname = True
                    else:
                        new_block.append(blk_line)
                # If no HostName line was found, insert one immediately after the Host line.
                if not found_hostname:
                    # Use a default indent of 4 spaces (adjust if needed)
                    indent = "    "
                    # Insert the new HostName line after the first line in the block.
                    new_block.insert(1, f"{indent}HostName {new_hostname}\n")
                updated_lines.extend(new_block)
            else:
                # Not the target host block; simply add the line.
                updated_lines.append(line)
                i += 1
        else:
            updated_lines.append(line)
            i += 1

    if not host_found:
        print(f"Error: Host entry '{target_host}' not found in SSH config.")
        sys.exit(1)

    # Write the updated config back to the file.
    with open(config_path, 'w') as f:
        f.writelines(updated_lines)
    print(f"Updated host '{target_host}' with HostName '{new_hostname}' in {config_path}.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: update_ssh_config.py <host_entry> <new_hostname>")
        sys.exit(1)

    host_entry = sys.argv[1]
    new_hostname = sys.argv[2]
    if host_entry not in ["engnode"]:
        raise ValueError(f"Are you sure? {host_entry}")
    update_ssh_config(host_entry, new_hostname)
