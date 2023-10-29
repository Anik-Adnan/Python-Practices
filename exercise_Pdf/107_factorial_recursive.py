def lambda_factorial(i): return 1 if i == 0 else i*lambda_factorial(i-1)


print(lambda_factorial(4))  # 4 * 3 * 2 * 1 = 12 * 2 = 24


def factorial(n):
    # n here should be an integer
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


factorial(0)
# out 1
factorial(1)
# out 1
factorial(2)
# out 2
factorial(3)
# out 6

# factorial = lambda n: 1 if n == 0 else n*factorial(n-1)
