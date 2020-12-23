#!/usr/bin/python

## use while loop and not recommended as there are some limitations

import sys

i=1
res=0
while (i!=len(sys.argv)):
    res +=int(sys.argv[i])
    i+=1
print 'sum of all values given in command line', res
