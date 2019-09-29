#!/usr/bin/env python3

from zip_parser import Zip
import matplotlib.pyplot as plt
import os
import sys

data = Zip.from_file(sys.argv[1])
counts = {}
for s in data.sections:
    try:
        compression_method = s.body.header.compression_method.name.lower()
        if compression_method not in counts:
            counts[compression_method] = {}
        first_byte = s.body.body[0]
        first_3_bits = "{0:b}".format(first_byte & 7).rjust(3, "0")
        if first_3_bits not in counts[compression_method]:
            counts[compression_method][first_3_bits] = 0
        counts[compression_method][first_3_bits] += 1
    except AttributeError:
        pass
xlim = max(map(lambda x: len(x), counts.values()))
for compression_method, count in counts.items():
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for first_3_bits, value in sorted_count:
        print(compression_method.rjust(12), ":", first_3_bits, ":", value)

    fig = plt.figure(frameon=False)
    ax = fig.add_subplot(111)

    plt.bar(range(len(sorted_count)), list(map(lambda x: x[1], sorted_count)), width=0.5, align='center')
    plt.xticks(range(len(sorted_count)), list(map(lambda x: x[0], sorted_count)))

    ax.set_xlim(-1,xlim)
    ax.set_xlabel('bit values')
    ax.set_ylabel('count', rotation='horizontal', ha='right')
    ax.set_title("Compression Method: {}".format(compression_method))

    fig.canvas.draw()
    plt.gca().set_position([0, 0, 1, 1])
    plt.savefig("{0}_count_{1}.svg".format(os.path.basename(sys.argv[1]), compression_method))
