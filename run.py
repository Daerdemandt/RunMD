#!/usr/bin/env python3

from runmd import parse_text, read_file
from pprint import pprint
import sys
import os

if __name__ == "__main__":
    if 2 == len(sys.argv):
        for command in parse_text(read_file(sys.argv[1])):
            os.system(command)
    else:
        print("Something is not ok! Did you forget to provide a filename?")
