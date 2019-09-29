#!/usr/bin/env bash

set -eux

xod=$1
[ -f "$xod" ]

xod_wd=./"wd_$(basename "$xod")"
mkdir -p "$xod_wd"

./kaitai_struct/extract_encrypted_bodies.py "$xod" "$xod_wd"

while read -r i; do
  mkdir -p "$(dirname "$xod_wd/decrypted/$i")"
  node extractor/decrypter.js "$xod_wd/encrypted/$i" "$i" "$xod_wd/decrypted/$i"
  mkdir -p "$(dirname "$xod_wd/inflated/$i")"
  cp "$xod_wd/decrypted/$i" "$xod_wd/inflated/$i"
done < <(cd "$xod_wd/encrypted/" && find . -type f | cut -c3-)

while read -r i; do
  node extractor/inflater.js "$xod_wd/decrypted/$i" "$xod_wd/inflated/$i"
done < <(cd "$xod_wd/needs_inflating/" && find . -type f | cut -c3-)

(cd "$xod_wd/inflated" && zip -r ../../"decrypted_$(basename "$xod")" ./*)
