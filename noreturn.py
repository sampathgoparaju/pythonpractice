#!/usr/bin/python

## This is for non return of the values defined inside the function.
## Values defined inside the function doesnt affect the global variables

def function(x,y):
    print 'This is non return function'
    print 'The value of x and y is %d and %d' %(x,y)
    print 'The address value of x and y is', id(x), id(y)
    x,y = 30,40
    print 'The address value of x and y after change is', id(x), id(y)
    print 'The value of x and y after change is %d and %d' %(x,y)

x=10
y=20
print 'The value of x and y is %d and %d' %(x,y)
print 'The address value of x and y is', id(x), id(y)
function(x,y)
print 'We passed x and y inside the function and that didnt affect the main variables, those are only for function alone'
print 'End of non return function program'
