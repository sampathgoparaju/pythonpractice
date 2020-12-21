#!/usr/bin/python

#this is the file having statements to be executed using the user defined modules
import UMbody as umb
x=input('Enter any numer:')
y=input('Enter any numer:')

print 'Addition of x and y is', umb.add(x,y)

print 'Subtraction of x and y is', umb.sub(x,y)

print 'Multiplication of x and y is', umb.mul(x,y)

print 'Division of x and y is', umb.div(x,y)

print 'the data values of a and b is', umb.a, umb.b
print 'END'
