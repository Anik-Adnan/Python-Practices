n = input().split("+")
n.sort()
for i in range(len(n)):
    if i != len(n)-1:
        print(n[i], end="+")
    else:
        print(n[i])
