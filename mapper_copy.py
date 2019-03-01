#!/usr/bin/python
import sys

for line in sys.stdin:
    A_i = 600
    B_j = 600
    line = line.strip()
    matrix,i,j,v = line.split(",")
    print '%s\t%s\t%s' % (i, j, j)
