#!/usr/bin/env bash

n=1
while [ $n -le 3 ]; do
	cp data.txt "backup_$n.txt"
	echo "Created backup_$n.txt"
	n=$((n+1))
	sleep 1
done
