import array
my_array = array.array('i' , [1, 2 , 4 , 6 ,8])

# add items
# append method
my_array.append(20)
print(my_array)

# insert(index, value) method
my_array.insert(6,10)
print(my_array)

# extend method 
# more than one value using extend() method.
my_extnd_array = array.array('i', [7,8,9,10])
my_array.extend(my_extnd_array)
print(my_array)

# fromlist() list add to an array
c=[11,12,13]
my_array.fromlist(c)
print(my_array)
# remove item
# remove(item_name)method
my_array.remove(2) 
print(my_array)

# pop method
# pop removes the last element from the array.
my_array.pop() # removed last item
my_array.pop(2) # removed index item my_array[2]= 6
print(my_array)

# index method
# index() returns first index of the matching value.
print(my_array.index(4)) # value 4 index = 1

# reverse method
my_array.reverse()
print(my_array)

# count method
print(my_array.count(8))

