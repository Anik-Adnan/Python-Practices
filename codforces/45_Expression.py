a = int(input())
b = int(input())
c = int(input())
max = 0
if a + (b + c) > max:
    max = a + (b + c)
if a + (b * c) > max:
    max = a + (b * c)
if a * (b + c) > max:
    max = a * (b + c)
if a * b * c > max:
    max = a * b * c
if (a + b) * c > max:
    max = (a + b) * c
if (a * b) + c > max:
    max = (a * b) + c

print(max)
