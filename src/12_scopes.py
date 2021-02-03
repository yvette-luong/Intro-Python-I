# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x # the `global` treats the x in line 9(x=99) equal to the x in line 5(x=12)
    x = 99
    print(x)
    print(id(x))
change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)
print(id(x))

# This nested function has a similar problem.


def outer():
    y = 120 # y is not global

    def inner():
        nonlocal y
    # y is local to the inner()
        y = 999
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
