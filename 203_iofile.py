# read file
# open function
# read method
# seek method
# tell method
# readlines method
# readline method
# close method

f = open('file1.text', 'r')  # by default r method

# print(f'corsor position {f.tell()}')
# print(f.read())
# print(f'corsor position {f.tell()}')

# print('before seek method')
# print(f.seek(0))

# print(f.read())
# print(f'corsor position {f.tell()}')

# print(f.readline(), end='')
# print(f.readline())
# print(f.readline())

# lines = f.readlines()
# print(lines) # print all lines in a list
# print(len(lines))  # 3 lines
# for i in lines:
#     print(i, end='')

for i in f:
    print(i, end='')

# file name
print(f.name)  # file1.text

# check file close ed or not ' return ture or false
print(f.closed)  # False
f.close()
