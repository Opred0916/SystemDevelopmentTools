#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv_file>" >&2
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: file not found: $1" >&2
    exit 1
fi

file="$1"

echo "Top 2 paths with most HTTP 5xx:"
awk -F, 'NR > 1 && $4 < 600 {count[$3]++} END {for (path in count) print count[path], path}' "$file" | sort -k1,1nr -k2,2 | head -n 2

echo "Average latency_ms:"
awk -F, 'NR > 1 {sum += $5; count++} END {printf "%.2f\n", sum/count}' "$file"
