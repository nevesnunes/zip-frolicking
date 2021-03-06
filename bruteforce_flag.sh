#!/bin/sh

set -eux

zip_file=$1
[ -f "$zip_file" ]
for i in $(seq 0 15); do
  mkdir -p "attempt_$i"
  cp "$zip_file" "attempt_$i"
  (
    cd "attempt_$i"
    ./patch.py "$zip_file" 6 "$i"
    binwalk -e "$zip_file"
  )
done
