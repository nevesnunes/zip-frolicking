# zip-frolicking

Scripts for analysing and modifying zip files:

- `./bruteforce_*.sh` - Attempt to extract file by iterating through all possible values for a given metadata property
- `./decrypt_xod.sh` - Create unencrypted xod file from an encrypted one
- `./kaitai_struct/aggregate_file_types.py` - Count files in zip with a given file extension and compression method
- `./kaitai_struct/count_first_3_bits_group_by_compression_method.py` - Visualize histograms of first 3 bits of each file's compressed data
- `./kaitai_struct/enumerate_files.py` - List files in a zip by index

### Dumping metadata fields and values

- `./kaitai_struct/dump_metadata.py` - Serializes and dumps kaitai object as json

One use case is to compare different zip files in a scriptable manner, for example, fields which aren't related to body size, using [gron](https://github.com/tomnomnom/gron) to compare entries in a line-oriented method:

```bash
diff -Nauw \
    <(./dump_metadata.py a.zip | gron | grep -v '\.\(un\)\?compressed_size') \
    <(./dump_metadata.py b.zip | gron | grep -v '\.\(un\)\?compressed_size') \
    | vim -c 'set filetype=diff' -
```

We can catch differences such as the comment bytes:

```diff
-json.sections[2].body.comment["py/b64"] = "bWFkZSBmb3IgdWl1Y3RmIGJ5IGt1aWxpbgAAAAAAAAA=";
+json.sections[2].body.comment["py/b64"] = "bWFkZSBmb3IgdWl1Y3RmIGJ5IGt1aWxpbiA6IF+kE0M=";
```

For comparing multiple files at a time, one can keep track of consistently different fields (e.g. size, global position...) and report files with fields that have an overall lower distinct count (e.g. among 10 files, only 1 had a comment).

```bash
printf '%s\n' \
    a.zip \
    b.zip \
    c.zip \
    | xargs -i bash -c './dump_metadata.py "$1" | gron | grep -v "\.\(un\)\?compressed_size"' _ {} \ 
    | sort | uniq -c | sort -n | vim -c 'set filetype=diff' -
```

Alternatives: [zipdetails](https://metacpan.org/pod/distribution/IO-Compress/bin/zipdetails), used in the CTF writeup: [UIUCTF 2020 - Zip Heck](https://ptomerty.xyz/writeups/2020-07-19-uiuctf-zip-heck/).
