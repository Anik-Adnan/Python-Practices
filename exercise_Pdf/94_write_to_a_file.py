# with open('myfile2.txt', 'w') as f:
#     f.write("Line 1")
#     f.write("Line 2")
#     f.write("Line 3")
#     f.write("Line 4")
# # Line 1Line 2Line 3Line 4

with open('myfile.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    f.write("Line 4\n")
# Line 1
# Line 2
# Line 3
# Line 4

# If you want to specify an encoding, you simply add the encoding parameter to the open function:
with open('my_file.txt', 'w', encoding='utf-8') as f:
    f.write('utf-8 text')

# It is also possible to use the print statement to write to a file. The mechanics are different in Python 2 vs Python 3,
# but the concept is the same in that you can take the output that would have gone to the screen and send it to a file
# instead.

with open('fred.txt', 'w') as outfile:
    s = "I'm Not Dead Yet!"
    print(s)  # writes to stdout
    print(s, file=outfile)  # writes to outfile
    # Note: it is possible to specify the file parameter AND write to the screen
    # by making sure file ends up with a None value either directly or via a variable
    myfile = None
    print(s, file=myfile)  # writes to stdout
    print(s, file=None)  # writes to stdout
