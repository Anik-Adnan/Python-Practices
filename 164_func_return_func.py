# function returning function
def outer_func():
    def inner_func():
        print("inside inner function")
    return inner_func


var = outer_func()  # outer_func return inner_func So, var==inner_func
print(var.__name__)  # inner_func
var()  # inside inner function


# def outer_func2():
#     def inner_func2():
#         print("inside inner function")
#     return inner_func2()


# var = outer_func2
# print(var.__name__)  # outer_func2
# var()  # inside inner function
# outer_func2()  # inside inner function


def outer_func3(msg):
    def inner_func3():
        print(f"outer function massage is {msg}")
    return inner_func3


var = outer_func3('"print with inner func"')
var()  # outer function massage is "print with inner func"
