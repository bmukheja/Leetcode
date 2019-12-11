#!/bin/bash
count=0
while IFS= read -r line;do
    count=$((count+1))
    if [ $count == 10 ];then
    	echo $line
    fi
done < file.txt
