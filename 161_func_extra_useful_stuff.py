# what are doc strings
# how to write docstring
# how to see docstrings
# what is help function

def add(a, b):
    '''this function takes 2 numbers and return their sum '''
    return a + b


print(add(2, 5))
print(add.__doc__)

# all function have a docstring
# len,sum,max,min,sorted,sum funtion
print(len.__doc__)
# print(sorted.__doc__)
# print(max.__doc__)
# print(sum.__doc__)

print(help(add))
print(add.__doc__)
print(help(sum))
