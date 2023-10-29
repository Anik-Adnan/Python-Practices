x = (1, 2, 3)
print(x[0])  # 1
print(x[1])  # 2
print(x[2])  # 3
# print(x[3])  # IndexError: tuple index out of range


# Indexing with negative numbers will start from the last element as -1:

print(x[-1])  # 3
print(x[-2])  # 2
print(x[-3])  # 1
# print(x[-4])  # # IndexError: tuple index out of range


# Indexing a range of elements
print(x[:-1])  # (1, 2)
print(x[-1:])  # (3,)
print(x[1:3])  # (2, 3)
