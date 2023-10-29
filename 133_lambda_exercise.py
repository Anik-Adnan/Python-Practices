# lambda practice

# def is_even(l):
#     if l%2==0:
#         return True
#     else:
#         return False

# def is_even(l):
#     return l%2==0
# print(is_even(5))
# print(is_even(4))

isEven= lambda a: a%2==0
print(isEven(8)) # True

last_char = lambda s: s[-1]
print(last_char("anik")) # k

# lambda with if else
# def func(s):
#     if len(s)>5:
#         return True
#     return False

func = lambda s: True if len(s)>5 else False
print(func('anik')) # false

func = lambda s:len(s)>5 
print(func('adnanbiswas')) # True
