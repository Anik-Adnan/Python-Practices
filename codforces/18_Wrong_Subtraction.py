a, b = map(int, input().split())
T = 1
while T <= b:
    if a % 10 != 0:
        a -= 1
    else:
        a /= 10
    T += 1
print(int(a))
