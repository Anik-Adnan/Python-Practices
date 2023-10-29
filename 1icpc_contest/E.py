t = int(input())
T = 1
while T <= t:
    n = int(input())
    a = list(map(int, input().split()))[:n]
    count = 0
    s = 0
    for i in range(n):
        for j in range(i + 1, n - 1):
            if a[i] > a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
                count += 1
    for i in a:
        if i > 0:
            s += i
    print(f"Case {T}: {s} {count}")
    T += 1
