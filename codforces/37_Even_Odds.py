n, k = map(int, input().split())
odd = (n + 1) // 2
if k <= odd:
    print(k * 2 - 1)
else:
    print((k-odd)*2)
