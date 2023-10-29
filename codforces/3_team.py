t = int(input())
T = 1
count = 0
while T <= t:
    n = map(int, input().split())
    a, b, c = n
    if (a and b and c) == 1 or (a and b) == 1 or (b and c) == 1 or (a and c) == 1:
        count += 1
    T += 1
print(count)
