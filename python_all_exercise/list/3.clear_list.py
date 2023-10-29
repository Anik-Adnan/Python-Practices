print("clear a list ")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.clear()
print("using clear methos :{} ".format(l))
l2 = [2, 3, 4, 5, 6, 6, 7]
l2 = []
print("using reinitialization : ", l)
l3 = [3, 4, 5, 6]
del l3[:]
print("using del :", l3)

l4 = [1, 2, 3, 4, 5, 6]
l4 *= 0
print("using *=0 : ", l4)
