#!/usr/bin/env python3

from zip_parser import Zip
import sys

data = Zip.from_file(sys.argv[1])
counts = {}
for s in data.sections:
    try:
        file_extension = '.'.join(s.body.header.file_name.split('.')[1:])
        if file_extension not in counts:
            counts[file_extension] = {}
        first_byte = s.body.body[0]
        if first_byte not in counts[file_extension]:
            counts[file_extension][first_byte] = 0
        counts[file_extension][first_byte] += 1
    except AttributeError:
        pass
for file_extension, count in counts.items():
    for first_byte, value in count.items():
        print(file_extension.rjust(12), ":", "{0:b}".format(first_byte).rjust(8), ":", value)
