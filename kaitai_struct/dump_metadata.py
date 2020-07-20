#!/usr/bin/env python3

# Usage:
# $0 ./file_to_parse

from zip_parser import Zip
import json
import jsonpickle
import sys

VALUE_MAX_LEN = 1024


def clean_value(value):
    if isinstance(value, str) and len(value) > VALUE_MAX_LEN:
        value = value[:VALUE_MAX_LEN] + " [and more {} bytes]".format(len(value) - VALUE_MAX_LEN)
    return value


def clean(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and len(value) > VALUE_MAX_LEN:
                data[key] = clean_value(value)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    value[i] = clean(item)
            elif isinstance(value, dict):
                data[key] = clean(value)
    return clean_value(data)


data = Zip.from_file(sys.argv[1])

serialized = jsonpickle.encode(data)
deserialized = json.loads(serialized)
clean_data = clean(deserialized)
print(json.dumps(clean_data, indent=4))
