my_list = [None] * 4
print(my_list)
my_list = ['test'] * 4
print(my_list)

my_list = [{1}] * 5
print(my_list)
# [{1}, {1}, {1}, {1}, {1}]

my_list[0].add(2)
print(my_list)
# [  {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}]

# Instead, to initialize the list with a fixed number of different mutable objects, use:
my_list = [{1} for _ in range(3)]
print(my_list)
