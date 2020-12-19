#!/usr/bin/python

##explicit calling of parameters

def explicit(a,b):
    print 'This is explicit calling of parameters'
    print 'The address value of a and b',  id(a), id(b)
    print 'the values of a and b is %d and %d' %(a,b)
    print 'End of function explicit'


x=input('Enter any number:')
y=input('Enter any number:')

print 'The address value of x and y', id(x), id(y)
print 'The values of x and y si %d and %d' %(x,y)
explicit(x,y)
print 'address and values of a,b,x an y are same'
print 'If parameters are not passed in the function name space then it will check in main namespace and execute'
print 'END'
