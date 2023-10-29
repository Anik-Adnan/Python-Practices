# remove(value) – removes the first occurrence of the specified value. If the provided value cannot be found, a
# ValueError is raised.

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.remove(0)
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
a.remove(9)
print(a)  # a: [1, 2, 3, 4, 5, 6, 7, 8]

# a.remove(10)
# ValueError, because 10 is not in a
