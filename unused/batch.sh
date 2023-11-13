#!/bin/bash

times=10

for i in $(seq $times)
do
	nohup ./automation.sh $1 $2 &
done
