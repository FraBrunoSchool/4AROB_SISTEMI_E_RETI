"""
1. If you do not understand this, go back through and use the comment trick to get it squared away in your mind.
   One simple English comment above each line will help you understand or at least let you know what you need to
   research more.
2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
3. There’s too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with
   just one target.write() command instead of six.
4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly
   say you want to write a file.
5. If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for
   Python’s open function and see if that’s true.

4/5. 'w' is the mode while opening a file. If not provided, it defaults to 'r' (open for reading in text mode).
     No, no, I don't need the target.truncate()

"""

# import a module
from sys import argv

# stores the values contained by argv
script, filename = argv

# print 3 string
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# input not memorized
input("?")

# other print
print("Opening the file...")

# open file
target = open(filename, 'w')

# simple print of a string
print("Truncating the file. Goodbye!")

# this line empties the file
target.truncate()

# print for ask 3 lines
print("Now I'm going to ask you for three lines.")

# 3 input for the lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# print which says it is starting to write to the file
print("I'm going to write these to the file.")

# write on the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# punto 3
target.write(line1 + "\n" + line1 + "\n" + line3 + "\n")

# print for says that the file will be closed
print("And finally, we close it.")

# close the file
target.close()

# punto 2
target = open(filename)
print("The contents of the file is: \n" + target.read())
