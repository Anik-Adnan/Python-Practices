# lambda expressions ( anonymous function)
def add(a,b):
    return a+b
# same with lambda
add2= lambda a,b: a+b
print(add2(10,20))

# we use lambda bulit-in function like map, reduce, filter

multiply = lambda a,b: a*b
print(multiply(4,6))

print(add) # <function add at 0x00F071D8>
print(add2) # <function <lambda> at 0x00F07190>
print(multiply) # <function <lambda> at 0x00F07148>