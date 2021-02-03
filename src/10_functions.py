# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    '''
    return num % 2 == 0 
    '''
# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
if is_even(num):
    print("Even Number!")
    # print(is_even(num))
else:
    print("Odd Number!")

# YOUR CODE HERE

