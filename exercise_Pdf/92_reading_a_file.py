# The simplest way to iterate over a file line-by-line:
with open('myfile1.text', 'r') as fp:
    for line in fp:
        print(line)
    fp.close()
# readline() allows for more granular control over line-by-line iteration. The example below is equivalent to the one
# above:
with open('myfile1.text', 'r') as fp:
    while True:
        cur_line = fp.readline()
        # If the result is an empty string
        if cur_line == '':
            # We have reached the end of the file
            break
        print(cur_line)
    fp.close()


# Using the for loop iterator and readline() together is considered bad practice.
# More commonly, the readlines() method is used to store an iterable collection of the file's lines:
with open("myfile1.text", "r") as fp:
    fp.seek(0)
    print(fp.tell())
    lines = fp.readlines()
    for i in range(len(lines)):
        print("Line " + str(i) + ": " + line)
    fp.close()
