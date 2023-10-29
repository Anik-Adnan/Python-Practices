import time

t1 = time.time()
data = [[1, 2], [3, 4], [5, 6]]
output = []
for each_list in data:
    for element in each_list:
        output.append(element)
print(output)
t2 = time.time()
print(t2-t1)
# Out: [1, 2, 3, 4, 5, 6]

# can be equivalently written as a list comprehension with multiple for constructs:

# t3 = time.time()
# data = [[1, 2], [3, 4], [5, 6]]
# output = [element for each_list in data for element in each_list]
# print(output)
# t4 = time.time()
# print(t4-t3)
# Out: [1, 2, 3, 4, 5, 6]

data = [[1], [2, 3], [4, 5]]
output = [element for each_list in data
          if len(each_list) == 2
          for element in each_list
          if element != 5]
print(output)
# Out: [2, 3, 4]


# data = [[1, 2], [3, 4], [5, 6]]
# def f():
#     output = []
#     for each_list in data:
#         for element in each_list:
#             output.append(element)
#     return output
# print(time.timeit(f()))

# 1000000 loops, best of 3: 1.37 μs per loop
# print(timeit([inner for outer in data for inner in outer]))

# 1000000 loops, best of 3: 632 ns per loop
