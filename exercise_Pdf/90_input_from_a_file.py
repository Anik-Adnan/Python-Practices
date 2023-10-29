# Input can also be read from files. Files can be opened using the built-in function open. Using a with <command> as
# <name> syntax (called a 'Context Manager') makes using open and getting a handle for the file super easy:

# with open('somefile.txt', 'r') as fileobj:
#     # write code here using fileobj
#     pass
# Files can be opened in different modes. In the above example the file is opened as read-only.
#  To open an existing file for reading only use r.
#  If you want to read that file as bytes use rb.
#  To append data to an existing file use a.
#  Use w to create a file or overwrite any existing files of the same name.
#  You can use r+ to open a file for both reading and writing.
#  The first argument of open() is the filename, the second is the mode. If mode is left blank, it will default to r.


# let's create an example file:
with open('shoppinglist.txt', 'w') as fileobj:
    fileobj.write('tomato\npasta\ngarlic')

with open('shoppinglist.txt', 'r') as fileobj:
    # this method makes a list where each line
    # of the file is an element in the list
    lines = fileobj.readlines()
print(lines)  # ['tomato\n', 'pasta\n', 'garlic']

with open('shoppinglist.txt', 'r') as fileobj:
    # here we read the whole content into one string:
    content = fileobj.read()
    # get a list of lines, just like int the previous example:
    lines = content.split('\n')
print(lines)  # ['tomato', 'pasta', 'garlic']


# If the size of the file is tiny, it is safe to read the whole file contents into memory. If the file is very large it is often
# better to read line-by-line or by chunks, and process the input in the same loop. To do that:
with open('shoppinglist.txt', 'r') as fileobj:
    # this method reads line by line:
    lines = []
    for line in fileobj:
        lines.append(line.strip())
print(lines)


# Opened files (fileobj in the above examples) always point to a specific location in the file.
fileobj = open('shoppinglist.txt', 'r')
pos = fileobj.tell()
print('We are at %u.' % pos)  # We are at 0.

# Upon reading all the content, the file handler's position will be pointed at the end of the file:
with open('shoppinglist.txt', 'r') as fileobj:
    content = fileobj.read()
    end = fileobj.tell()
    print('This file was %u characters long.' % end)
    # This file was 22 characters long.
    fileobj.close()

# The file handler position can be set to whatever is needed:
fileobj = open('shoppinglist.txt', 'r')
fileobj.seek(7)
pos = fileobj.tell()
print('We are at character #%u.' % pos)


# You can also read any length from the file content during a given call. To do this pass an argument for read().
# When read() is called with no argument it will read until the end of the file. If you pass an argument it will read that
# number of bytes or characters, depending on the mode (rb and r respectively):
# reads the next 4 characters
# starting at the current position
next4 = fileobj.read(5)
# what we got?
print(next4)  # 'cucu'
# where we are now?
pos = fileobj.tell()
print('We are at %u.' % pos)  # We are at 12, as we was at 7, and read 4 chars.
fileobj.close()

# To demonstrate the difference between characters and bytes:
with open('shoppinglist.txt', 'r') as fileobj:
    print(type(fileobj.read()))  # <class 'str'>
with open('shoppinglist.txt', 'rb') as fileobj:
    print(type(fileobj.read()))  # <class 'bytes'>
