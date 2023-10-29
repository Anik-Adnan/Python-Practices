l = [20, 10, 20, 4, 100]
l.sort()
print("using sort() minimum num is :   ", l[0])
print("using min() minimum num is :", min(l))
l2 = [10, 80, 500, 600, 400, 900, 73]


def min_num(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min


print("using function minimum num is : ", min_num(l2))
