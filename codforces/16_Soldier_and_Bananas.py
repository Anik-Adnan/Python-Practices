k, n, w = map(int, input().split())
total_dollars = 0
for i in range(1, w + 1):
    total_dollars += i * k
if total_dollars > n:
    print(total_dollars - n)
else:
    print(0)
