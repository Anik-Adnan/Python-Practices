# n = map(int, input().split())

n = [1, 2, 3, 4, 45, 89, 500]


def swap_list(l):
    # temp = l[0]
    # l[0] = l[-1]
    # l[-1] = temp
    l[0], l[-1] = l[-1], l[0]

    return l


print("Swap first in last element {}".format(swap_list(n)))
