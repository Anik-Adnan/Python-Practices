# merged = list1 + list2
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)
print(alist + blist)
# Output:
# a1 b1
# a2 b2
# a3 b3

# If the lists have different lengths then the result will include only as many elements as the shortest one:
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3', 'b4']
for a, b in zip(alist, blist):
    print(a, b)
# Output:
# a1 b1
# a2 b2
# a3 b3
alist = []
print( len(list(zip(alist, blist))) )
# Output:
# 0