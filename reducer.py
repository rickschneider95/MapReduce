#!/usr/bin/env python
#Version 1


###simple entry-wise multiplication
#goal: generate a list with same keys, loop through each of these lists and caluclate result value

import sys

#initialize index:
previous_key = None
#initialize list:
calc_list = []

for line in sys.stdin:
    #strip and get the values in each line (i.e. the key, the index and the value)
    line = line.strip()
    key, ind, v = line.split("\t")
    #error-prone type conversion to integer:
    try:
        ind = int(ind)
        v = int(v)
    except ValueError:
        continue
    
    #case where the key is the same than the last one 
    if (key == previous_key):
        calc_list.append(v)
    #case where index changes and previous key != None (i.e. not the beginning of the algorithm):
    elif previous_key:
        i=0
        output = 0
        while i<len(calc_list)-1:
            output = output + calc_list[i]*calc_list[i+1]
            i=i+2
        print "%s\t%s"%(previous_key,output)
        #empty list, as first key is over now:
        calc_list = []
        #initialize empty list with first vnew value
        calc_list.append(v)
        #update previous key:
        previous_key = key
    #case where prev_key is None (i.e. at the very beginning of the algorithm):
    else:
        #initialize the previous_key:
        previous_key = key
        #initialize th elist with the first value:
        calc_list.append(v)

#the last list needs to be treated as well:   
if key == previous_key:
        i=0
        output = 0
        while i<len(calc_list)-1:
            output = output + calc_list[i]*calc_list[i+1]
            i=i+2
        print "%s\t%s"%(previous_key,output)


#Why move to v2?
#->if, elif, else can be sumarized in way easier and shorter code!
#->missing treatment for sparse matrices


###links with map reduce implemenation:

#https://github.com/amberm291/MatrixMultiplyMR

#https://github.com/AiningWang/Matrix-Multiplication-using-MapReduce
#->naive and smart implemenation

#
