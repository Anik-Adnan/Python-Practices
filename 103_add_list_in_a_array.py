# Add items from list into array using fromlist() method
import array
my_array = array.array('i' , [1, 2 , 4 , 6 ,8])

# fromlist method
c=[11,12,13]
my_array.fromlist(c)
# 11,12 and 13 were added from list c to my_array.
print(my_array)