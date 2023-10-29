n, k = map(int, input().split())
contestan = list(map(int, input().split()))
score = contestan[k-1]
count = 0
for i in range(n):
    if contestan[i] >= score and contestan[i] > 0:
        count += 1
print(count)
