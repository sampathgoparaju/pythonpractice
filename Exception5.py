#!/usr/bin/python

# Exception handling 
try:
    x=input("Enter any number:")
    y=input("Enter any number:")
    try:
        print 'The values of x and y are', x,y
        res=x/y

        print 'The output of the division is', res
        print "I have executed"

    except ZeroDivisionError,e:
        print 'Internal::ZDE:Error encountered, trying to divide number by zero',e

except (NameError,TypeError),e:
    print 'External::The error message is',e
except Exception,e:
    print 'Default:This is a default exception',e   
