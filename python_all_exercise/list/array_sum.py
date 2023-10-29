# n = map(int, input().split())

n = [1, 2, 3, 4, 45, 89, 500]


def sum_all(l):
    sum = 0
    for i in l:
        sum += i
    return sum


print("Sum osf array is {}".format(sum_all(list(n))))
