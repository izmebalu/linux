#!/bin/bash
fname=$1
if [ ! -e $fname ]; then
	echo "test: $fname: No such file or directory"
fi
if [ -d $fname ]; then
        echo "test: $fname: it is a directory"
fi
if [ ! -s $fname ]; then
        echo "test: $fname: It is an empty file"
fi
count=1
while read line
do
	echo "    $count   $line"
	let count++
done < $fname
