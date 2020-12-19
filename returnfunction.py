#!/usr/bin/python

## This is for return of the values defined inside the function.


def function(x,y):
    print 'This is a return function'
    print 'The value of x and y is %d and %d' %(x,y)
    print 'The address value of x and y is', id(x), id(y)
    x,y = 30,40
    print 'The address value of x and y after change is', id(x), id(y)
    print 'The value of x and y after change is %d and %d' %(x,y)
    return(x,y)

x=10
y=20
print 'The value of x and y is %d and %d' %(x,y)
print 'The address value of x and y is', id(x), id(y)
x,y=function(x,y)
print 'Now values have been returned to main namespace'
print 'The value of x and y after return is %d and %d' %(x,y)
print 'The address value of x and y after return is', id(x), id(y)
print 'We passed x and y inside the function and those are returned to the main variables'
print 'End of return function program'
