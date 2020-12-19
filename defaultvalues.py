#!/usr/bin/python

#passing default values in the function

def Default(x=0,y=2):
    print 'The default function executing'
    print 'The default values of x and y is %d and %d' %(x,y)
    return x+y, x-y

print 'this is the main function'
x,y=Default()
print 'The default values of x and y is %d and %d' %(x,y)


#Now, we are passing values to the arguments list

x=10;y=5
print 'The values of x and y is %d and %d' %(x,y)
x,y=Default(x,y)
print 'The values of x and y is %d and %d' %(x,y)

x=100
print 'The values of x and y is %d and %d' %(x,y)
x,y=Default(x,y)
print 'The values of x and y is %d and %d' %(x,y)
