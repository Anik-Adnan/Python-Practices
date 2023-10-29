import math
t = int(input())
T = 1
while T <= t:
    n = map(int, input().split())
    a, b, m = n
    count = 0
    for i in range(m + 1):
        k = math.gcd(a + i, b + i)
        if k == 1:
            count += 1

    print(f"Case {T}: {count}")
    T += 1
