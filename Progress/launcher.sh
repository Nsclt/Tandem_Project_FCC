#!/bin/bash 


coefficient = ${1?Error: need coefficient}
center_of_mass = ${2?Error: chose center of mass energy}
stepspace = ${3?Error: provide the space between the steps}
positivesteps = ${4?Error: How far do you want to go into the positive values}
negativesteps = ${5?Error: How far do you want to go into the negative values}
scriptname = ${6?Error: Name the used script}
outputdir = ${7?Error: Name your output directory}

python commands.py $1 $2 $3 $4 $5 $6 $7
./mg5_aMC $6

echo ''coefficient'' $1 >> $7/info.txt
echo ''Beam energy'' $2 >> $7/info.txt
echo ''distance between steps'' $3 >> $7/info.txt
echo ''number of steps fr positive values'' $4 >> $7/info.txt
echo ''number of steps fr negative values'' $5 >> $7/info.txt

echo 'I got till this point'

