# zip function
user_id = ['user1', 'user2', 'user3']
names = ['anik', 'adnan', 'biswas']
last_name = ['khan', 'chowdhary', 'sami']
# print(zip(user_id, names)) # <zip object at 0x000001FCA2518DC0>
print(list(zip(user_id, names)))
print(dict(zip(user_id, names)))

print(list(zip(user_id, names, last_name)))
# print(dict(zip(user_id, names, last_name)))  # error


# example = [('a', 1), ('b', 2), ('c', 3)]
# print(dict(example)) # {'a': 1, 'b': 2, 'c': 3}
