
import operator
a = 21
b = 5

# add method
print(operator.add(a,b))
print(a+b)
d = operator.iadd(a, b)
print(d)
# div, __truediv__ method
# truediv , floordiv 
print(operator.__truediv__(a,b))
print(operator.truediv (a,b))
print(operator.floordiv(a, b))
print(a / b)
print(a//b) # int floor division

from operator import truediv
print(truediv(a, b))

