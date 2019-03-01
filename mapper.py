#!/usr/bin/env python
import sys

#actual mapping algorithm that needs A_i, B_i and text file as input
for line in sys.stdin:
    A_i = 600
    B_j = 600
    line = line.strip()
    matrix,i,j,v = line.split(",")

    if matrix == "A":
        for ind in range(1,B_j+1):
            key = i + "," + str(ind)
            print "%s\t%s\t%s"%(key,j,v)
            #we use tab to get rid of the problem of negative number
    else:
        for ind in range(1,A_i+1):
            key = str(ind) + "," + j
            print "%s\t%s\t%s"%(key,i,v)
