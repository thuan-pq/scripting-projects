#!/usr/bin/bash

while read line
do
    echo $line
done < $1 # $1 is first argument pass to command line
# Do not print last line
