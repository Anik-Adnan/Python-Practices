from math import sqrt
C, H = 50, 30

D = input().split(',')
D = list(map(lambda d: str(int(sqrt(2*C*int(d)/H))), D))
print(",".join(D))
