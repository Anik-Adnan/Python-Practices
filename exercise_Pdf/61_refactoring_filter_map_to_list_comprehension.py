# even numbers < 10
# f = [x for x in range(10) if x % 2 == 0]
f = filter(lambda x: x % 2 == 0, range(10))
print(list(f))

# multiply each number by two
# print([2*x for x in range(10)])
print(list(map(lambda x: 2 * x, range(10))))
print(list(map(lambda x: x % 2 == 0, range(10))))  # return bool

# Map & Filter
filtered = filter(lambda x: x % 2 == 0, range(10))
results = map(lambda x: 2 * x, filtered)
print(list(results))  # [0, 4, 8, 12, 16]
# List comprehension
results = [2*x for x in range(10) if x % 2 == 0]
print(results)  # [0, 4, 8, 12, 16]


# sum of all elements in list
# sum = reduce(lambda x, y: x+y, range(10)) # showing error
# print(sum)

# # Refactoring - Quick Reference
# # Map
# map(F, S) == [F(x) for x in S]
# # Filter
# filter(P, S) == [x for x in S if P(x)]
# # where F and P are functions which respectively transform input values and return a bool
