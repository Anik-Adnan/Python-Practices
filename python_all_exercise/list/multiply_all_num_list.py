import math
from functools import reduce


def multiplyList(myList):

    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [1, 2, 3]
print(multiplyList(list1))

list2 = [3, 2, 4]
result2 = reduce((lambda x, y: x * y), list2)
print(result2)


# math
list2 = [3, 2, 4]


result2 = math.prod(list2)
print(result2)
