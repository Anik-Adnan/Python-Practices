n = int(input())
g = list(map(int, input().split()))[:n]
for i in range(1, len(g) + 1):
    for j in g:
        if i == j:
            print(g.index(j)+1, end=" ")
print()
