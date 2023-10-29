def multipy_num(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply*=i
    return multiply
list=[1,2,3,4]
# print(multipy_num(list)) # [1, 2, 3, 4]
# print(*list) # 1 2 3 4 unpacked list element
print(multipy_num(*list)) # 24

tuple=(4,5,5)
print(multipy_num(*tuple))