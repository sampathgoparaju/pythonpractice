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
    print 'ZDE:Error encountered, trying to divide number by zero'
except NameError,e:
    print 'NE:The given variable is not defined in program'
except TypeError,e:
    print 'TE:The given variable is not compatible'
except Exception,e:
    print 'Default:This is a default exception',e   
