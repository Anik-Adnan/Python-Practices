# pop([index]) – removes and returns the item at index. With no argument it removes and returns the last
# element of the list.

a = [1, 2, 3, 4, 5, 6]

print(a.pop(2))
print(a)
# Returns: 5
# a: [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
# a.pop(8)
# print(a)  # a = [1, 2, 3, 4, 5, 6]

# With no argument:
print(a.pop())
print(a)
# Returns: 6
# a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
