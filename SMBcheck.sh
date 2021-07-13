#!/bin/bash

input=$1
while IFS= read -r line
do
        echo $line
        echo exit | smbclient -L \\\\$line

done < "$input"
