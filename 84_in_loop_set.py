b = {1,2,3,4,5,5,4,5,7,9,8,7,10}

# if 10 in b:
#     print('present')

# for item in b:
#     print(item)

# set operation

a ={1,2,3, 4, 5}
c = {4 , 5 , 6, 7}
# intersection (& operator)
print(a.intersection(c))
print(a & c)

# union( or | operator),
print(a.union(c))
print(a | c)

# difference
print(a.difference(c))
print(a - c)

# symmetric difference
print(a.symmetric_difference(c))
print(a ^ c)

x = {1, 2, 4}
y ={ 2, 4}
# issuperset check
print(x.issuperset(y))
print(x >= y)

# issubset check
print(x.issubset(y))
print(x <= y)

# disjoint (check any one element present in both set )
print(x.isdisjoint(y)) #false
p={1, 2}
o = {3, 4}
print(p.isdisjoint(o)) # true

# len function
print(len(p))

