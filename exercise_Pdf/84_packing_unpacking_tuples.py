# a = 1, 2, 3 # a is the tuple (1, 2, 3)
# and
# a = (1, 2, 3) # a is the tuple (1, 2, 3)
# are equivalent. The assignment a = 1, 2, 3 is also called packing because it packs values together in a tuple.
# Note that a one-value tuple is also a tuple. To tell Python that a variable is a tuple and not a single value you can use
a = 1  # a is the value 1
a = 1,  # a is the tuple (1,)

# A comma is needed also if you use parentheses
a = (1,)  # a is the tuple (1,)
a = (1)  # a is the value 1 and not a tuple
# To unpack values from a tuple and do multiple assignments use

# unpacking AKA multiple assignment
x, y, z = (1, 2, 3)
# x == 1
# y == 2
# z == 3
# The symbol _ can be used as a disposable variable name if one only needs some elements of a tuple, acting as a
# placeholder:
a = 1, 2, 3, 4
_, x, y, _ = a
# x == 2
# y == 3

# Single element tuples:
x, = 1,  # x is the value 1
x = 1,  # x is the tuple (1,)


# In Python 3 a target variable with a * prefix can be used as a catch-all variable (see Unpacking Iterables ):
# Python 3.x Version ≥ 3.0
first, *more, last = (1, 2, 3, 4, 5)
print(first)  # first == 1
print(more)  # more == [2, 3, 4]
print(last)  # last == 5
