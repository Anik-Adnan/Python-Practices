# f= open('file1.text')
# f.read()
# f.close()

# with block
# context manager

with open('file1.text') as f:
    data = f.readlines()
    print(data)
print(f.closed)  # true # becasue autometic file is closed using with operation
