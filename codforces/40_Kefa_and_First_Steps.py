n = int(input())
day = list(map(int, input().split()))[:n]
count = 1
max = 0
for i in range(n - 1):
    if day[i] <= day[i + 1]:
        count += 1
    else:
        if max < count:
            max = count
        count = 1
if max < count:
    max = count

print(max)
