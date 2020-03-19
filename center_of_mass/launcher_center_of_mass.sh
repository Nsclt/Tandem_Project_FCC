#!/bin/bash

coefficient = ${1?Error: need coefficient}
coef_value = ${2?Error: need value you want to give the coefficient}
scriptname = ${3?Error: need scriptname}
outputdir = ${4?Error: need output directory}

python center_of_mass.py $1 $2 $3 $4
./mg5_aMG $3

echo ''coefficient'' $1 >> $5/center_info.txt 
echo ''coef_value'' $2 >> $5/center_info.txt 
