#/bin/bash
while read line; do
	if [ ${line:4}=='-' && ${line:8}=='-' ]; then
		echo $line;
	fi
done < file.txt
