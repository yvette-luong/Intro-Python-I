"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open("foo.txt")
read_file = f.read()
print(read_file)
# print(f.closed)
print(f"'f.close?' {f.closed}")
f.close()
print(f"'f.close?' {f.closed}")

print("\n---NEW WAY---")
with open("foo.txt") as f:
    # this level -local to with statement
    read_file = f.read()
    print(read_file)

print(" FILE IS CLOSED ")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain


# "w" over write data
# "a" append data
# "x" create files
# "r" for reading files
# YOUR CODE HERE

with open("bar.txt", "w") as file_input:
    file_input.write("Arbitrary line 1\n")
    file_input.write("Arbitrary line 2\n")
    file_input.write("Arbitrary line 3\n")
with open("bar.txt", "r") as file_output:
    print("bar.txt after creation")
    print(file_output.read())
