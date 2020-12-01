"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
#  JAVA SCRIPT
# console.log('x is 10, y is 2.25, z is "I like turtles!"')
# console.log(`x is ${x}, y is ${y}, z is ${z}`)
# PY
# %.2f means 2 decimal for that float cause y = 2.24552 should print out 2.25
print('Using the Printf Operator method to print x is %d, y is %.2f, z is "%s"' % (x ,y ,z)) 

# Use the 'format' string method to print the same thing
print('Using the Format String method to print x is {}, y is {}, z is "{}"' .format(x ,"%.2f"%y ,z)) 
print('Using the Format String method and Round to print x is {}, y is {}, z is "{}"' .format(x ,round(y,2) ,z)) 

# Finally, print the same thing using an f-string
print(f'Using the F-string method to print x is {x}, y is {"%.2f"%y}, z is "{z}"')