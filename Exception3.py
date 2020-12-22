#!/usr/bin/python

# Exception handling 
try:
    x=input("Enter any number:")
    y=input("Enter any number:")

    print 'The values of x and y are', x,y

    res=x/y

    print 'The output of the division is', res
    print "I have executed"

except ZeroDivisionError:
    print 'Error encountered, trying to divide number by zero'
except NameError,e:
    print 'The given variable is not defined in program'
    print 'The default message is ',e
