# A string can reversed using the built-in reversed() function, which takes a string and returns an iterator in reverse
# order.

print(reversed('hello'))
# <reversed object at 0x0000000000000000>
print([char for char in reversed('hello')])
# ['o', 'l', 'l', 'e', 'h']

# reversed() can be wrapped in a call to ''.join() to make a string from the iterator.
print(''.join(reversed('hello')))
# 'olleh'

# While using reversed() might be more readable to uninitiated Python users, using extended slicing with a step of
# -1 is faster and more concise. Here , try to implement it as function:


def reversed_string(main_string):
    return main_string[::-1]


print(reversed_string('hello'))
# 'olleh'
