n = int(input())
col = list(map(int, input().split()))
col.sort()
for i in col:
    print(i, end=" ")
print()
