my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky', 'nerdy', 'geek', 'love',
           'questions', 'words', 'life']

# Yield successive n-sized
# chunks from l.


def divide_chunks(l, n):

    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


# How many elements each
# list should have
n = 5

# list comprehension
x = list(divide_chunks(my_list, n))
print(x)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# How many elements each
# list should have
n = 4

# using list comprehension
x = [l[i:i + n] for i in range(0, len(l), n)]
print(x)

y = [l[i:i + n] for i in range(0, len(l))]
print(y)
