#!/usr/bin/python

##using str.isdigit to avoid string in between whil adding parameters

import sys


print 'The parameters given in the command line', sys.argv
print 'The length of the parameters in the command line', len(sys.argv)

i=1
res=0

while (i!=len(sys.argv)):
    print "sys.argv[%d]: %s" %(i,sys.argv[i])
    if (sys.argv[i].isdigit()):
        res +=int(sys.argv[i])
    i+=1

print 'The total sum of integer values in the command line', res
