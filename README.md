# zip-frolicking

Scripts for analysing and modifying zip files:

- `./bruteforce_*.sh` - Attempt to extract file by iterating through all possible values for a given metadata property
- `./decrypt_xod.sh` - Create unencrypted xod file from an encrypted one
- `./kaitai_struct/aggregate_file_types.py` - Count files in zip with a given file extension and compression method
- `./kaitai_struct/count_first_3_bits_group_by_compression_method.py` - Visualize histograms of first 3 bits of each file's compressed data
- `./kaitai_struct/enumerate_files.py` - List files in a zip by index
