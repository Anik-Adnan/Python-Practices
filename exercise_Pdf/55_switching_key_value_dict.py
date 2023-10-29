my_dict = {1: 'a', 2: 'b', 3: 'c'}
# you wanted to swap the keys and values you can take several approaches depending on your coding style:

# swapped = {v: k for k, v in my_dict.items()}
# print(dict((v, k) for k, v in my_dict.items()))

# swapped = dict(zip(my_dict.values(), my_dict))
# swapped = dict(zip(my_dict.values(), my_dict.keys()))

swapped = dict(map(reversed, my_dict.items()))
print(swapped)
# Out: {a: 1, b: 2, c: 3}
