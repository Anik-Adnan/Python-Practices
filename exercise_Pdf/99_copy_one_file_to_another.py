# Copying contents of one file to a dierent file

with open('myfile1.text', 'r') as in_file, open('copy.txt', 'w') as out_file:
    for line in in_file:
        out_file.write(line)


# Using the shutil module:
# import shutil
# shutil.copyfile(src, dst)
