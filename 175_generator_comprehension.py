# same as list comprehension just add first parenthesis
# square = [i ** 2 for i in range(1, 11)]

square = (i ** 2 for i in range(1, 11))

# for num in square:
#     print(num)
# for num in square: # only one time can gnenerate
#     print(num)

# print(*square) unpacked square

print(next(square))  # 1
print(next(square))  # 4
print(next(square))  # 9
print(next(square))  # 16
