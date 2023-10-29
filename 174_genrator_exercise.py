def even_gen(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield (i)


even = even_gen(10)
# print(*even_gen(10)) # 2 4 6 8 10 2 4 6 8 10
# print(*even) # 2 4 6 8 10

# for i in even:
#     print(i, end=' ')


for i in even_gen(10):
    print(i, end=' ')
