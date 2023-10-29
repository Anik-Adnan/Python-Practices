def makeInc(x):
    def inc(y):
        # x is "attached" in the definition of inc
        return y + x
    return inc


incOne = makeInc(1)
incFive = makeInc(5)
print(incOne(5))  # returns 6
print(incFive(5))  # returns 10


# def makeInc2(x):
#     def inc2(y):
#         # incrementing x is not allowed
#         x += y
#         return x
#     return inc2


# incOne = makeInc2(1)
# incOne(5)  # UnboundLocalError: local variable 'x' referenced before assignment

# Python 3 offers the nonlocal statement (Nonlocal Variables ) for realizing a full closure with nested functions.


def makeInc3(x):
    def inc3(y):
        nonlocal x
        # now assigning a value to x is allowed
        x += y
        return x
    return inc3


incOne = makeInc3(1)
print(incOne(5))  # returns 6
