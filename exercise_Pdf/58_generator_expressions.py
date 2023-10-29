# Generator expressions are very similar to list comprehensions. The main difference is that it does not create a full
# set of results at once; it creates a generator object which can then be iterated over.


# list comprehension
print([x**2 for x in range(10)])
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Python 2.x Version ≥ 2.4

# generator comprehension
g = (x**2 for x in range(10))
print(g)  # Output: <generator object <genexpr> at 0x11b4b7c80>
print(list(g))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# These are two very different objects:
# the list comprehension returns a list object whereas the generator comprehension returns a generator.
# generator objects cannot be indexed and makes use of the next function to get items in order.

# for i in [x**2 for x in range(10)]:
#     print(i)

# for i in (x**2 for x in range(10)):
#     print(i)
