#!/usr/bin/env bash

trap 'echo ClEAN_EXIT >> cleanup.log; exit 0' TERM

n=0
while true; do
	echo "$n"
	n=$((n+1))
	sleep 1
done
