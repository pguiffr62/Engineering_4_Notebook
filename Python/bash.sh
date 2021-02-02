#!/bin/bash

gpio -g write 17 0
gpio -g write 18 0
counter=1

while [ $counter -le 10 ]
do
	echo $counter
	counter=$(( $counter + 1 ))
	gpio -g  mode 17 out
	gpio -g  write 17 1
	gpio -g  mode 18 out
        gpio -g  write 18 1
	sleep 2
	gpio -g  mode 17 out
	gpio -g  write 17 0
	gpio -g  mode 18 out
        gpio -g  write 18 0
done



