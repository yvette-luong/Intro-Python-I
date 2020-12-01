"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12
# YOUR CODE HERE

# convert string to an interger
# method 1:
# y = int(y)
# print(y + x)

# method 2 -  value unchanging method
print(x+int(y))

# method 3 :
z = int(y)
print(x+z)

# Write a print statement that combines x + y into the string value 57
# YOUR CODE HERE

# method 1 - convert integer into string
# x = str(x)
# y = str(y)
# print( x + y )

# method 2
# print(str(x) +str(y))

# method 3 - value unchanging method
print(str(x)+y)
