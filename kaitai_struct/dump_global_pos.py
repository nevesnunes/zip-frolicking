#!/usr/bin/env python3

from zip_parser import Zip
import sys

data = Zip.from_file(sys.argv[1])
counts = {}
for i, s in enumerate(data.sections):
    # LocalFile
    try:
        file_extension = '.'.join(s.body.header.file_name.split('.')[1:])
        compression_method = s.body.header.compression_method
        global_pos = s.global_pos
        if file_extension not in counts:
            counts[file_extension] = {}
        counts[file_extension][i] = {
            'compression_method': compression_method,
            'global_pos': global_pos
        }
    except AttributeError:
        # LocalDir
        try:
            file_extension = '.'.join(s.body.file_name.split('.')[1:])
            compression_method = s.body.compression_method
            global_pos = s.global_pos
            if file_extension not in counts:
                counts[file_extension] = {}
            counts[file_extension][i] = {
                'compression_method': compression_method,
                'global_pos': global_pos
            }
        except AttributeError:
            pass
for file_extension, count in counts.items():
    for i, value in count.items():
        print('{0:#x}'.format(value['global_pos']))
        #print(file_extension.rjust(12), ":", str(i).rjust(8), ":", value['global_pos'], ":", value['compression_method'])
