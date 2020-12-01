# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
# x.append(y)
# ASSIGNMENT (=) method : # x = x + y

x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
# in python, if you just use pop() -> it will remove the last item, but if you put the index inside the () it will remove the index instead
x.pop(4)
# x.pop(-3)
# x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000 - OUTPUT: [1000, 2000, 3000, 4000, 9000, 99000, 10000]
# YOUR CODE HERE
# for num in x:
#     print(num * 1000)

# list comprehension
# this code is to format the bumber into array, have to put the actual body of the for loop first which means 'num', and then put the 'for` statement
demoA = [ num + 2 for num in x]
print( 'An extra demo - Print all the values in x + 5 =',demoA )
demoB = [ num * 1000 for num in x]
print( 'An extra demo - Print all the values in x * 1000 =',demoB)