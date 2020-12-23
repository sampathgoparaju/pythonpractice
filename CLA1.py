#!/usr/bin/python

#!using argv command line interface
## from sys import argv- this is recommended one

import sys

print 'Total parameters given at command line:', len(sys.argv)
print 'Given values in command line',sys. argv
print 'first parameter at command line', sys.argv[0]
print 'second parameter at command line',sys.argv[1]
print 'type of value of the first index', type(sys.argv[1])
