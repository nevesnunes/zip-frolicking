#!/usr/bin/env python3

# Usage:
# $0 file_to_extract work_directory_for_output

from zip_parser import Zip
import os
import sys

data = Zip.from_file(sys.argv[1])
with open(sys.argv[1], "r+b") as f:
    for i, s in enumerate(data.sections):
        # LocalFile
        try:
            filename = sys.argv[2] + '/encrypted/' + s.body.header.file_name
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w+b") as f:
                f.write(s.body.body)

            compression_method = s.body.header.compression_method
            if compression_method.name.lower() == 'deflated':
                filename = sys.argv[2] + '/needs_inflating/' + s.body.header.file_name
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, 'a'):
                    os.utime(filename, None)
        except AttributeError:
            pass
