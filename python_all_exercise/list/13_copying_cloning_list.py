l = [1, 2, 3, 44, 55, 66]

# using slicing
newl = l[:]  # too much fast sliciing
print(newl)

# usiing extend
newl2 = []
newl2.extend(l)
print(newl2)

# using list method
newl3 = list(l)
print(newl3)

# list cpomprehension
new4 = [i for i in l]
print(new4)


new5 = l.copy()
print(new5)
