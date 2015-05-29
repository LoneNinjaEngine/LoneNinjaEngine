#!/bin/sh

PATH=/apps/opt/python.34
export $PATH

if [ -f LoneNinjaEngine.py ]
then
   echo "LoneNinjaEngine Available"
      
   if [ -f inputfile.txt ]
   then
	echo "Input File Available"
	if [ -d rt-polaritydata ]
		echo "Dictionary Available"
   	then
		python LoneNinjaEngine.py	
   	else
      		echo "rt-polaritydata Not Available"
      		quit
   	fi
   else
      echo "inputfile.txt Not Available"
      quit
   fi
else
      echo "LoneNinjaEngine Not Available"
	quit
fi

