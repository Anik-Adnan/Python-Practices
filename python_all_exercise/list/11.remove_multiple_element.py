l = [1, 2, 3, 4, 5, 6, 77, 8, 99, 33]
for i in l:
    if i % 2 == 0:
        l.remove(i)
print("new list : ", l)

l = [11, 22, 33, 44, 55, 66, 77, 88]
l = [i for i in l if i % 2 != 0]
print("comprehension : ", l)

del l[0:3]
print("using del new list : ", l)

l = [1, 2, 3, 4, 55, 6, 7, 8]
un_wanted = {55, 3, 6}
new_list = [i for i in l if i not in un_wanted]
print(" removing un wnted num : ", new_list)

l = [1, 2, 3, 4, 55, 6, 7, 8]
un_wanted = {0, 3, 4, 5}
for i in sorted(un_wanted, reverse=True):
    del l[i]
print(*l)
