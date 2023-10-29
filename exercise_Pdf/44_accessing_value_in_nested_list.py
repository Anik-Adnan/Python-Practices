# Starting with a three-dimensional list:

alist = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]
# Accessing items in the list:
print(alist[0][0][1])
# 2
# Accesses second element in the first list in the first list

print(alist[1][1][2])
# 10

# Accesses the third element in the second list in the second list
# Performing support operations:
alist[0][0].append(11)
print(alist[0][0][2])
# 11
# Appends 11 to the end of the

# Using nested for loops to print the list:

# for row in alist:  # One way to loop through nested lists
#     for col in row:
#         print(col)

#[1, 2, 11]
#[3, 4]
#[5, 6, 7]
#[8, 9, 10]
#[12, 13, 14]

# Another way to use nested for loops. The other way is better but I've needed to use this on occasion:
for row in range(len(alist)):  # A less Pythonic way to loop through lists
    for col in range(len(alist[row])):
        print(alist[row][col])
#[1, 2, 11]
#[3, 4]
#[5, 6, 7]
#[8, 9, 10]
#[12, 13, 14]

# list comprehension or even as a generator to produce efficiencies, e.g.:
print([col for row in alist for col in row])
#[[1, 2, 11], [3, 4], [5, 6, 7], [8, 9, 10], [12, 13, 14]]

# Not all items in the outer lists have to be lists themselves:
alist[1].insert(2, 15)
# print(alist)
# [[[1, 2, 11], [3, 4]], [[5, 6, 7], [8, 9, 10], 15, [12, 13, 14]]]
# Inserts 15 into the third position in the second list


# Using slices in nested list:
print(alist[1][1:])
#[[8, 9, 10], 15, [12, 13, 14]]
# Slices still work


# The final list:
print(alist)
#[[[1, 2, 11], [3, 4]], [[5, 6, 7], [8, 9, 10], 15, [12, 13, 14]]]
