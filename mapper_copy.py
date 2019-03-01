#!/usr/bin/python
import sys

for line in sys.stdin:
    A_i = 600
    B_j = 600
    line = line.strip()
    matrix,i,j,v = line.split(",")
    for ind in range(1,B_j+1):
        key = str(i) + "," + str(ind)
