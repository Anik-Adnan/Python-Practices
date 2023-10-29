import array
my_array = array.array('u' , ['g','e','e','k'])

# tostring() 
# converts the array to a string.
print(my_array.tostring()) 

# tolist()
my_array = array.array('i', [1,2,3,4,5])
print(my_array.tolist())

# fromlist() 
my_array = array.array('c' , ['g','e','e','k'])
print(my_array.fromstring('forgeeks'))
