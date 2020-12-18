#!/usr/bin/python

##using multiple functions

def functionhi():
    print 'Hi World'
    print 'function hi ends'
    functionhello()
    print 'END OF FUNCTIONS'

def functionhello():
    print 'Hello Universe'
    print 'function hello ends'

print 'Calling functions inside functions'
functionhi()
print 'End of multi functions'
