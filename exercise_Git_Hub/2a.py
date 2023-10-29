# using function
def fact_func(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


n = int(input())
print(fact_func(n))
