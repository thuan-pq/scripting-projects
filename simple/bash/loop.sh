#!/usr/bin/bash

echo "While loop"
i=0
while [[ $i -le 10 ]];
do
    echo "$i"
    (( i += 1 ))
done

echo -e "\nFor loop"
for i in {1..5}
do
    echo $i
done
