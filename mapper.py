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


###idea:
#1)add combiner, i.e. local aggregation
#2)implement normal matrix multiplication and test (i.e. triple for loop --> time O(n^3) , enormous memory consumption; as not distributed, no advantage of sparsity), 
# see http://www.joefkelley.com/853/ 
# also compare advantage of sparsity
#The first is based on the fact that if you store the matrixes as a tuples (i, j, x) meaning aij=x, 
#then the multiplication is equivalent to a relation algebra join followed by a group by and aggregation.
# 
# change log
# 1)   
