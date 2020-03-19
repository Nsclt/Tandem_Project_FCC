#!/bin/bash 


coefficient = ${1?Error: need coefficient}
center = ${2?Error: chose center of mass energy}
stepspace = ${3?Error: provide the space between the steps}
total_steps = ${4?Error: How many steps do you need?}
scriptname = ${5?Error: Name the used script}
outputdir = ${6?Error: Name your output directory}

python OtB_commands.py $1 $2 $3 $4 $5 $6 
./mg5_aMC $5

echo ''coefficient'' $1 >> $6/info.txt
echo ''Energy per beam'' $2 >> $6/info.txt
echo ''distance between steps'' $3 >> $6/info.txt
echo ''number of steps fr positive values'' $4 >> $6/info.txt
echo ''number of steps fr negative values'' $5 >> $6/info.txt