l = [20, 10, 20, 4, 100]
l.sort()
print("using sort() max is :   ", l[-1])
print("using max() max num is :", max(l))
l2 = [10, 80, 500, 600, 400, 900, 73]


def max_num(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max


print("using function max num is : ", max_num(l2))
