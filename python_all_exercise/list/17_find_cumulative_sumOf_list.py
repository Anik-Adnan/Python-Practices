l = [10, 20, 30, 40, 50]


def cumulative(l):
    new_list = []
    sum = 0
    for i in range(len(l)):
        sum += l[i]
        new_list.append(sum)
    return new_list


print("cumulative sum : ", cumulative(l))

# using sum function


def Cumulative(lists):
    cu_list = []
    cu_list = [sum(lists[0:x]) for x in range(len(l)+1)]
    return cu_list[1:]


print("cumulative sum : ", Cumulative(l))
