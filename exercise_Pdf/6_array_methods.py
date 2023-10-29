import array
my_array = array.array('i', [1, 2, 3, 4, 5])
my_extnd_array = array.array('i', [7, 8, 9, 10])

# append method
my_array.append(6)
print(my_array)
# array('i', [1, 2, 3, 4, 5, 6])

# insert method
my_array.insert(4, 10)
print(my_array)
# array('i', [1, 2, 3, 4, 10, 5, 6])

# extend method
my_array.extend(my_extnd_array)
print(my_array)
# array('i', [1, 2, 3, 4, 10, 5, 6, 7, 8, 9, 10])

# fromlist method  # convert list to array
c = [11, 12, 13]
my_array.fromlist(c)
print(my_array)
# array('i', [1, 2, 3, 4, 10, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# remove method
my_array.remove(10)  # removed 10
print(my_array)
#array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# del statement # delete one or more items from an array
del my_array[2:5]  # delete 3, 4, 5
print(my_array)

# pop method
my_array.pop()  # return last element
print(my_array)  # removed last element 13

# index method # index() returns first index of the matching value
print(my_array.index(10))  # index = 9

# reverse method
my_array.reverse()
print(my_array)

# buffer_info() method provides you the array buffer start address in memory and number of elements in array
print(my_array.buffer_info())
# (2197025685936, 12)
# (address, number_of_element)

# count() # return number of times and element appears in an array
my_array.append(5)
print(my_array.count(5))  # 5 have 2 times

# # tostring # convert array to string
# my_char_array = array.array('u', ['g', 'e', 'e', 'k'])
# # array('c', 'geek')
# print(my_char_array.tostring())
# # geek

# tolist method
my_array = array.array('i', [1, 2, 3, 4, 5])
c = my_array.tolist()
print(c)
# [1, 2, 3, 4, 5]

# # fromstring method
# my_char_array = array.array('u', ['g', 'e', 'e', 'k'])
# my_char_array.fromstring("stuff")
# print(my_char_array)
# #array('c', 'geekstuff')
