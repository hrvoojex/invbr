#!/usr/bin/env python
# coding: utf-8

import sys

input_file = raw_input("Input file name: ")
try:
    data = open(input_file, "r")
except:
    print("No such file %s" % input_file)
    sys.exit("Quitting...")
count = 1
for line in data:
    line = line.rstrip()
    line = line.split(" ")
    if len(line) > 1:
        line[1] = line[1] + str(''.join(chr(ord('0')) for i in xrange(10 - len(line[1]) - len(str(count))))) + str(count)
    else:
        line.append((str(''.join(chr(ord('0')) for i in xrange(10 - len(str(count)))))) + str(count))
    count += 1
    print '{0:10s} {1:20s}'.format(line[0], line[1])