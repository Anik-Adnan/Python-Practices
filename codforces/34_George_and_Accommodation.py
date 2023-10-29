n = int(input())
t = 1
count = 0
while t <= n:
    a, b = map(int, input().split())
    free_sit = b - a
    if free_sit >= 2:
        count += 1
    t += 1
print(count)
