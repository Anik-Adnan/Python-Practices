num = int(input())
sum = 0
if num < 0:
    num = abs(num)
    s = 1
else:
    pass
while num != 0:
    sum = sum*10+num % 10
    num = num // 10
if s == 1:
    print(sum * -1)
else:
    print(sum)
