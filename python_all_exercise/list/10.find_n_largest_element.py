from functools import reduce
l = [1000, 298, 3579, 100, 200, -45, 900]
n = 4

l.sort()
print(l)
print(l[-n:])

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l.sort(reverse=True)
print(l[:n])
