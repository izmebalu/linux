#!/bin/bash
while [ true ]
do
	read -p "Enter any file name: " fname
        if [ -f $fname ]; then
		echo "The content of $fname is: "
		echo ".................................."
		cat $fname
		echo ".................................."
	else:
		echo "There is no file exists with file or directory"
	fi
	read -p "Do you want to check for any other file [Yes/No]: " option

	case $option in
		[yY]|[yY][eE][sS])
			continue
			;;
		[nN]|[nN][oO])
			break
			;;
	esac

done
echo "Thanks for using application"

