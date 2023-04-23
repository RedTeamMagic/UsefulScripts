#!/bin/bash

for port in {1..65535}; do
  status=$(ssh -q -o BatchMode=yes -o ConnectTimeout=1 localhost -p $port "echo 2>/dev/null" >/dev/null 2>&1 && echo "open" || echo "closed")
  echo "Port $port is $status"
done
