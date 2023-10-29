# any all
number1 = [1, 3, 5]
number2 = [2, 4, 6]
number3 = [1, 2, 4, 7]

# even1 = []
# for num in number1:
#     even1.append(num % 2 == 0)
# print(even1) # [False, False, False]
# print(any(even1)) # False

# all element are even than print true
print(all([num % 2 == 0 for num in number2]))
# all element are odd than print true
print(all([num % 2 != 0 for num in number1]))

# all element are not even print false
print(all([num % 2 == 0 for num in number3]))

# any of  element are  even print true
print(any([num % 2 == 0 for num in number3]))
