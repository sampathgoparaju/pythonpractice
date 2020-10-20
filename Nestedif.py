#NestedIf statements

#!/usr/bin/python

x=raw_input('Enter any value:')
y=raw_input('Enter any value:')
z=raw_input('Enter any value:')

if x>y:
    if x>z:
        print 'x is the biggest value:',x
    else:
        print 'z is the biggest value:',z

else:
    if y>z:
        print 'y is the biggest value:',y
    else:
        print 'z is the biggest value:',z
   
print('Nested If statements program')
