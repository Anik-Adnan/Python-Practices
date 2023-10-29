L = [-5, -2, -1, 0, 1, 2]
a = -1
b = len(L)
while True:
    h = (a+b)//2  # // is the integer division, so h is an integer
    if L[h] == -1:
        print(h)
        break
    elif L[h] > -1:
        b = h
    elif L[h]:
        a = h
