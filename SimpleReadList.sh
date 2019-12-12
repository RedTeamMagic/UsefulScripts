#!/bin/bash

input=$1
while IFS= read -r line
do
        #host $line
        echo $line

done < "$input"
