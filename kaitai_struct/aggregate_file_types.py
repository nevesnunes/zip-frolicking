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
        counts[file_extension][i] = compression_method
    except AttributeError:
        pass
for file_extension, count in counts.items():
    for i, value in count.items():
        print(file_extension.rjust(12), ":", str(i).rjust(8), ":", value)
