# math , cmath , operator
# pow mwthod 
a,b = 2,3
import math,operator
print(a ** b) # result int
c= 3
print(pow(a,b,c)) # (a ** b) % c == 2
print(operator.pow(a,b)) # result int 

print(math.pow(a,b)) # result float , does not allow complex results
print(math.pow(16, 1/2)) #  root 16 =4
print(math.pow(32, 1/5)) # 2^5 = 32

# secial function
# sqrt mwthod 
import cmath
c=4
print(math.sqrt(c)) # float 
print(cmath.sqrt(c)) # complex (2+0j)

# math.exp(x) computes (e ** x)
print(math.exp(0)) # 1.0
print(math.exp(1)) # 2.718281828459045(e)

# math.expm1(x) computes e ** x -1
print(math.exp(8)-1)
print(math.expm1(0))

print(math.exp(1e-6)-1)
print(math.expm1(1e-6))