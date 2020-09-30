#!/bin/bash
while [ true ]
do
	read -p "Enter Employee number: " eno
	read -p "Enter Employee name: " ename
	read -p "Enter Employee salary: " esal
	read -p "Enter Employee place: " eplace

	echo "$eno:$ename:$esal:$eplace" >> emp.txt

	read -p "Do you want to another employee data[Yes/No]: " option

	case $option in
		[yY]|[yY][eE][sS])
			continue
			;;
		[nN]|[nN][oO])
			break
			;;
	esac
done
echo "Open emp.txt to see the information"


