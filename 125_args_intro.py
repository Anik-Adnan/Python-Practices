# make flexible functions
# *operator
# *args

def total(a,b):
    return a+b
# print(total(10,20,30,40)) # typr error

def all_toal(*args):
    # print(args) #(1, 2, 5, 10, 15)
    # print(type(args)) # <class 'tuple'>
    total= 0
    for num in args:
        total+=num
    return total

print(all_toal(1,2,5,10,15))
