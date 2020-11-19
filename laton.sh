#!/bin/bash
lat="NULL"
lon="NULL" 
color=0
silent=0
printonly=0
rm ../maps_output.txt 
touch ../maps_output.txt 
while getopts 'c:ps' arg;
 do
	case ${arg} in 
	c) echo 'color set to mode' ${OPTARG}; color=$OPTARG;; 
	p) echo 'mode set to print only'; printonly=1;;
	s) echo 'silent mode enabled'; silent='1';;
	?) echo 'uknown option'; exit 7;;  

 esac
done
#create config file for settings like color 
echo $color >  ../config.txt 



for dir in *$pwd
 do
	echo "[latitude longitude] -- file: $dir:"
	read lat lon
	
	cat $dir | awk -F',' '{$1='$lat'; $2='$lon'; print $1, $2, $3, $4}' >> ../thiccboi.txt  
 done
#call python script to organize and find the duplicates - > temp.txt
cd .. 
touch temp.txt config.txt 
python sort_macs.py
#sed 1i"red|blue|green|orange|yellow" ../maps_output.txt> ../maps_output.txt
if [ $printonly == '0' ] 
then
 python maps.py 
 echo 'done'
 firefox Map.html
	if [ $silent == '0' ]
	then
 	cat maps_output.txt
	fi 
else
 echo 'done'
 cat maps_output.txt 
fi 
#clean up 
 rm temp.txt 
 rm config.txt 
 rm thiccboi.txt 
