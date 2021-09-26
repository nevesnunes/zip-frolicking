#!/usr/bin/env python3

# Usage:
# $0 ./file_to_parse

from zip_parser import Zip
import sys

data = Zip.from_file(sys.argv[1])
filename = data.sections[0].body.header.file_name
with open(filename + ".deflate", "wb") as f:
    f.write(data.sections[0].body.body)
