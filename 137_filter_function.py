# filter function
# def is_even(a):
#     return a%2==0
num = [3, 5, 7, 6, 4, 2, 8, 10, 11, 15, 16, 1]
# even=tuple( filter(is_even,num))

even = tuple(filter(lambda a: a % 2 == 0, num))
print(even)

even = [i for i in num if i % 2 == 0]
print(even)

# even= filter(lambda a: a%2==0 ,num)
# print(even) # filter object
# for i in even:
#     print(i)
# # map ,filter iterable only one times wiithout iterable_name(list,tuple,dic)
# for j in even:
#     print(j)

