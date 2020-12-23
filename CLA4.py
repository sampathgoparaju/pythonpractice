#!/usr/bin/python

#!using argv command line interface
## from sys import argv- this is recommended one

import sys

print 'Total parameters given at command line:', len(sys.argv)
print 'Given values in command line', sys.argv
print 'first parameter at command line', sys.argv[0],type(sys.argv[0])
print 'second parameter at command line',sys.argv[1],type(sys.argv[1])
print 'third paramter value at command line',sys.argv[2],type(sys.argv[2])
print 'The addition of two parameters', (sys.argv[1])+(sys.argv[2])
print 'The addition of two parameters using eval', eval(sys.argv[1])+eval(sys.argv[2])
print 'The result of adding two parameters using int', int(sys.argv[1])+int(sys.argv[2])
