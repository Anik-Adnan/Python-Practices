# map function
# map(function_name , iterable(list,tuple,set,dic)_name)

numbers = [1, 2, 3, 4]

# map with function
# def square(a):
#     return a**2
# square=list(map(square,numbers))
# print(square)

# map with lambda
square = list(map(lambda a: a**2, numbers))
print(square)

# list comprehension
# square=[i**2 for i in numbers]
# print(square)

# normal
# square = []
# for i in numbers:
#     square.append(i**2)
# print(square)

name = ['abc', 'abcd', 'abcde', 'abcdef']
length = list(map(len, name))
print(length)  # [3, 4, 5, 6]
