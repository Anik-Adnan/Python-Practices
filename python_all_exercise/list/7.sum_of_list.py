l = [1, 2, 3, 4, 5]
print("using sum() sum is : ", sum(l))


def sum_all(l):
    sum = 0
    for i in l:
        sum += i
    return sum


print("using sum_all sum of list is  ", sum_all(l))
