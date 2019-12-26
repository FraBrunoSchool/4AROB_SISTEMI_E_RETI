"""
1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
3. Combine input with argv to make a script that gets more input from a user. Don’t overthink it. Just use argv to get
   something, and input to get something else from the user.
4. Remember that modules give you features. Modules. Modules. Remember this because we’ll need it later.

1. The error is this:
    Traceback (most recent call last):
        File "ES_13.py", line 4, in <module>
            script, first, second, third = argv
    ValueError: not enough values to unpack (expected 4, got 2)
    -it says that the right arguments were not passed when the script was started
2. More arguments
#   >>> script, first, second, third, fourth = argv
   Fewer arguments
#   >>> script, first, second = argv
"""

from sys import argv

# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# punto 3
name = input("Nome: ")
print("Ciao " + name + " hai scritto ed esuguito uno script di nome " + script)
