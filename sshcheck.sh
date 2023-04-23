#!/bin/bash

for port in {1..65535}; do
  ssh -q -o BatchMode=yes -o ConnectTimeout=1 localhost -p $port "echo 2>/dev/null" >/dev/null 2>&1
  if [ $? -eq 0 ]; then
    echo "SSH is running on port $port"
  fi
done
