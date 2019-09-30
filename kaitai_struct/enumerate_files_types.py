#!/usr/bin/env python3

from zip_parser import Zip
import sys

data = Zip.from_file(sys.argv[1])
counts = {}
for i, s in enumerate(data.sections):
    try:
        file_name = s.body.header.file_name
        compression_method = s.body.header.compression_method
        if file_name not in counts:
            counts[file_name] = {}
        counts[file_name][i] = compression_method
    except AttributeError:
        pass
for file_name, count in counts.items():
    for i, value in count.items():
        print(str(i).rjust(8), ":", str(value).rjust(24), ":", file_name)
