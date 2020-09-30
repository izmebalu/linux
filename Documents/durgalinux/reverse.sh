#!/bin/bash
read -p "Enter the string to reverse: " str
output=''
len=$(echo -n $str | wc -c)
while [ $len -ge 1 ]
do
	x=$(echo -n $str | cut -c $len)
	output=$output$x
	let len--
done
echo "The reversed string is: $output "
echo "The original string is: $str "

