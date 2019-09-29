#!/usr/bin/env python3

from zip_parser import Zip
import sys

data = Zip.from_file(sys.argv[1])
with open(sys.argv[1], "r+b") as f:
    for i, s in enumerate(data.sections):
        # LocalFile
        try:
            compression_method = s.body.header.compression_method
            global_pos = s.global_pos
            f.seek(global_pos + 6)
            f.write(bytes([1]))
        except AttributeError:
            # LocalDir
            try:
                compression_method = s.body.compression_method
                global_pos = s.global_pos
                f.seek(global_pos + 8)
                f.write(bytes([1]))
            except AttributeError:
                pass
