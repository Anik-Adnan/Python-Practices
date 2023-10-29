def sum_all(d):
    sum = 0
    for i in d:
        sum = sum + d[i]
    return sum


d = {'a': 100, 'b': 200, 'c': 300}
print(sum_all(d))
