import math, cmath
print(math.log(5)) # float 1.6094379124341003
print(cmath.log(5)) # complex
print(math.log(5, math.e)) #1.6094379124341003

print(math.log(1000, 10)) # base 10 ,resulr float 2.9999999999999996
print(math.log(1000,10)) # base 10 result complex (2.9999999999999996+0j)

print(math.log1p(5)) ## Logarithm base e - 1 (higher precision for low values)
print(math.log2(8)) # Logarithm base 2
print(math.log10(1000)) # Logarithm base 10
print(cmath.log10(1000))