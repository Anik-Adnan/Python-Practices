n = int(input())
coins = list(map(int, input().split()))
sum = sum(coins) / 2
coins.sort(reverse=True)
s = 0
count = 0
for i in coins:
    s += i
    if s <= sum:
        count += 1
    else:
        count += 1
        break
print(count)
