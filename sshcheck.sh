#!/bin/bash

# define the IP address or hostname to check
HOST="127.0.0.1"

# loop through every port number from 1 to 65535
for PORT in $(seq 34460 65535); do
  # use ssh to connect to the host on the current port
 ssh -4 -p "$PORT" "$HOST"
  # check the exit status of the ssh command
  if [ $? -eq 0 ]; then
    # if the ssh connection was successful, print the port number
    echo "SSH connection successful on port $PORT"
  fi
done
