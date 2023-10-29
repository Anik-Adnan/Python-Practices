# append, insert, extend, pop, remove, reverse, clear, copy, del 
a = [1, 2, 3, 4]

# append method
# # Append an element of a different type, as list elements do not need to have the same type
# b = 'anik'
# c = ['Adnan']
# a.append(b)
# print(a)
# a.append(c)
# print(a)

# extend method
# Extend list by appending all elements from b
b = [8, 9]
a.extend(b) # extsnd just element
print(a)
a.extend(range(3)) # add 0, 1, 2
print(a)

# index
print(a.index(8))
# insert(index, value)
a.insert(2, 100)
print(a)

# pop([index]) – removes and returns the item at index.
print(a.pop(2)) # return index value 100
print(a) # removed index 2

# remove 
a.remove(2)
print(a)

# reverse
a.reverse()
print(a)

# count 
print(a.count(1))

# sort() 
# sorts the list in numerical and lexicographical order and returns None.
a.sort()
print(a)
a.sort(reverse= True)
print(a)

# clear 
b = [10 , 20 , 30]
b.clear()
print(b)

# replication
b = ['anik'] * 3
print(b)

# del method
a = list(range(10))
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[: : 2] # [2, 4, 6, 8] deleted
print(a) # [1, 3, 5, 7, 9]
del a[-1] # deleted last element
print(a)
del a[:] # all deleted
print(a) # [] empty list

# copying
a = list(range(11))
print(a)
b = a # copy a to b
print(b)
c = a[:] # copy all item
print(c)
print(c[::-1]) # rverse order

import copy
x = [10 , 15, 20]
new_list = copy.copy(x) # x copied new_list
print(new_list) # slower than list()
new = copy.deepcopy(x) # slowest and most memory-needing method
print(new)