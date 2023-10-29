# The preferred method of file i/o is to use the with keyword. This will ensure the file handle is closed once the
# reading or writing has been completed.
with open('myfile1.text') as in_file:
    content = in_file.read()
    print(content)

# or, to handle closing the file manually, you can forgo with and simply call close yourself:
in_file = open('myfile1.text', 'r')
content = in_file.read()
print(content)
in_file.close()
