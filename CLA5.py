#!/usr/bin/python

## from sys import argv- this is recommended one
#using IF ELSE command, but is not recommended any where.. It is just for learning purpose.

import sys

if len(sys.argv)== 3:

    print 'Total parameters given at command line:', len(sys.argv)
    print 'Given values in command line', sys.argv
    print 'The addition of two parameters using eval', eval(sys.argv[1])+eval(sys.argv[2])
else:
    print 'please give three arguments'
