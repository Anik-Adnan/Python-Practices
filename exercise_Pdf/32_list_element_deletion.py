a = list(range(10))
del a[::2]
print(a)
# a = [1, 3, 5, 7, 9]

del a[-1]
print(a)  # a = [1, 3, 5, 7]

del a[:]
print(a)  # a = []
