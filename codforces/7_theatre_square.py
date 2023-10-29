import math
n, m, a = i = map(int, input().split())
if n % a == 0:
    ncount = n // a
else:
    ncount = (n // a) + 1
if m % a == 0:
    mcount = m // a
else:
    mcount = (m // a) + 1

print(ncount*mcount)
nn = math.ceil(n/a)
mm = math.ceil(m/a)
print(nn*mm)
