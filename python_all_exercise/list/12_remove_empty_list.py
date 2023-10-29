l = [1, 2, 3, 4, 5, [], 33, [], 44, 22, [], 11, [], 33]
print("list:"+str(l))
# using list coorehension
res = [i for i in l if i != []]
print("new list : ", res)
# using filter
newl = list(filter(None, l))
print("using filter : ", newl)
