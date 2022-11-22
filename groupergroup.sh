#!/bin/bash

#firefox & 

input=$1
lines=$(wc -l <$input)
counter=0
var=10
zero=0

echo Total lines: $lines

while IFS= read -r line
do	
	let "counter++"
	#host $line
        echo Opening: $line
	current=$(expr $lines - $counter)
	echo $current
	firefox --new-tab $line
	
	breakcheck=$(expr $counter % $var)
	echo $breakcheck
	echo $zero
	if [ $breakcheck -eq $zero ]
	then
		read -p "press any key to continue..." < /dev/tty
	fi

done < "$input"
