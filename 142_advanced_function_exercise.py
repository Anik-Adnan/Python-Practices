# def average_finder(a, b):
#     avg = []
#     for pair in zip(a, b):
#         avg.append(sum(pair) / len(pair))
#     return avg

# print(average_finder([1, 2, 3], [4, 5, 6]))


def average_finder(*args):
    avg = []
    for pair in zip(*args):
        avg.append(sum(pair) / len(pair))
    return avg


print(average_finder([1, 2, 3], [4, 5, 6], [7, 8, 9]))

# 2 lines
average = lambda *args: [sum(pair) / len(pair) for pair in zip(*args)]
print(average([1, 2, 3], [4, 5, 6], [7, 8, 9]))
