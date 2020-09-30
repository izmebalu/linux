#!/bin/bash
read -p "Enter any number: " num
x=1
while [ $x -le $num ]
do
	if [ $x -eq 5 ]; then
		break
	fi
	echo $x
	let x++
done

 

