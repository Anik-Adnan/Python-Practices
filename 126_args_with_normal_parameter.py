# args with normal parameter
def multipy_num(num, *args):
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(multipy_num(2,2,3))