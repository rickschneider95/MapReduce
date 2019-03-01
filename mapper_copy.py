#!/usr/bin/env python
import sys


for line in sys.stdin:
    A_i = 600
    B_j = 600
    line = line.strip()
    matrix,i,j,v = line.split(",")

    if matrix == "A":
        for ind in range(1,B_j+1):
            key = i + "," + str(ind)
            print '%s\t%s\t%s' % (key, j, v)

    else:
        for ind in range(1,A_i+1):
            key = str(ind) + "," + j
            print '%s\t%s\t%s' % (key, i, v)
