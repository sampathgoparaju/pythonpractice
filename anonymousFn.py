#!/usr/bin/python

#how to use anonymous function

add = lambda x,y:x+y

a=10
b=20
c= add(a,b)
print 'The values of a,b anc is %d, %d and %d' %(a,b,c)

a=10.5
b=20.3
c= add(a,b)
print 'The values of a,b anc is %f, %f and %f' %(a,b,c)

a='e'
b='f'
c= add(a,b)
print 'The values of a,b anc is %s, %s and %s' %(a,b,c)
type(add)

