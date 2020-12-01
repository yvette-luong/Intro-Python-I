"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
# This demo pull information from computer and have it run through here ! 

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# for(let i=0; i< sys.argv.length; i++){
#     console.log(sys.argv[i]);
# }
for item in sys.argv:
    print(item)

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())