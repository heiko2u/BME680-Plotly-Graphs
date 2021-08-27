#!/bin/bash

test=$(ps -aux | grep temp | wc -l)


echo $test


while [ "$test" -eq "2" ];

do
test=$(ps -aux | grep temp | wc -l)

:

done


zenity --error --text="Data Aquisision failed"
