def sort_list(list1, list2):
    zipped_pair = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pair)]
    return z


x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0,   1,   1,    0,   1,   2,   2,   0,   1]

print(sort_list(x, y))

x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [0,   1,   1,    0,   1,   2,   2,   0,   1]

print(sort_list(x, y))


# using dictionary
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

final_list = []
dic = {list1[i]: list2[i] for i in range(len(list1))}
sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
for i in sorted_dic.keys():
    final_list.append(i)
print(final_list)
