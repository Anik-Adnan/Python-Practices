lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
for idx, s in enumerate(lst):
    print("%s has an index of %d" % (s, idx))


for i in range(2,4):
    print("lst at %d contains %s" % (i, lst[i]))

for s in lst[1::2]:
    print(s)
for i in range(1, len(lst), 2):
    print(lst[i])