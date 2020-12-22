#!/usr/bin/python

# Exception handling 
try:
    x=input("Enter any number:")
    y=input("Enter any number:")

    print 'The values of x and y are', x,y

    res=x/y

    print 'The output of the division is', res
    print "I have executed"

except ZeroDivisionError,e:
    print 'Error encountered, trying to divide number by zero'
    print 'standard error message: ',e
    print 'The type of e object is ', type(e)
