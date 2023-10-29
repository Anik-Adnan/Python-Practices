import array
my_array = array.array('i' , [1, 2 , 4 , 6 ,8])

# buffer_info() method
# This method provides you the array buffer start address in memory and number of elements in array.
print(my_array.buffer_info())
# print (address , number_of_element)
