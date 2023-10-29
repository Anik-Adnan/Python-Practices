import array
my_array = array.array('i', [1, 2, 3, 4, 5])
# print(my_array[1])
# # 2
# print(my_array[2])
# # 3
# print(my_array[0])
# # 1


for i in my_array:
    print(i)

a = list(map(lambda i: str(i), my_array))
print(*a)
print(','.join(a))
