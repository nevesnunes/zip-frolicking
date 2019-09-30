#!/usr/bin/env python3

from zip_parser import Zip
import sys

data = Zip.from_file(sys.argv[1])
counts = {}
for i, s in enumerate(data.sections):
    try:
        file_extension = '.'.join(s.body.header.file_name.split('.')[1:])
        compression_method = s.body.header.compression_method
        if file_extension not in counts:
            counts[file_extension] = {}
        if compression_method not in counts[file_extension]:
            counts[file_extension][compression_method] = 0
        counts[file_extension][compression_method] += 1
    except AttributeError:
        pass
for file_extension, count in counts.items():
    for i, value in count.items():
        print(file_extension.rjust(12), ":", str(value).rjust(8), ":", i)
