# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001,1111
# Then the output should be:
# 1010,1111

value = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)

print(','.join(value))


# or
# def check(x):                       # converts binary to integer & returns zero if divisible by 5
#     total,pw = 0,1
#     reversed(x)

#     for i in x:
#         total+=pw * (ord(i) - 48)   # ord() function returns ASCII value
#         pw*=2
#     return total % 5

# data = input().split(",")           # inputs taken here and splited in ',' position
# lst = []

# for i in data:
#     if check(i) == 0:               # if zero found it means divisible by zero and added to the list
#         lst.append(i)

# print(",".join(lst))

# or
# def check(x):                   # check function returns true if divisible by 5
#     return int(x,2)%5 == 0      # int(x,b) takes x as string and b as base from which
#                                 # it will be converted to decimal
# data = input().split(',')

# data = list(filter(check,data)) # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
# print(",".join(data))

# or
data = input().split(',')
# lambda is an operator that helps to write function of one line
data = list(filter(lambda i: int(i, 2) % 5 == 0, data))
print(",".join(data))


# or
data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))
