# create generator with generator function
# 1) generator function

# 10 , print 1-10
def num(n):
    for i in range(1, n + 1):
        yield(i)


# for n in num(10):
#     print(n)
num10 = num(10)

# num10 = list(num(10))
for num in num10:
    print(num)
# for num in num10:
#     print(num)
