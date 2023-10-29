a, b = map(int, input().split())
count_year = 0
while a <= b:
    a *= 3
    b *= 2
    count_year += 1
print(count_year)
