list = [ 1, 2, 3, 4, 5 , 6 ,7 ,8 ,9 ,10]
# print [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]

# new_list = []
# for i in list:
#     if i %2 ==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

print( [ i*2 if i%2==0 else -i for i in list])