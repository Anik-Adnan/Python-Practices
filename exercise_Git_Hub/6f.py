from math import sqrt
C, H = 50, 30
mylist = input().split(',')
print(*(round(sqrt(2*C*int(D)/H)) for D in mylist), sep=",")
