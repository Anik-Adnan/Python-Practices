d = {}
# To add items to a dictionary, simply create a new key with a value:
d['newkey'] = 42  # {'newkey': 42}
print(d)

# It also possible to add list and dictionary as value:
d['new_list'] = [1, 2, 3]
print(d)  # {'newkey': 42, 'new_list': [1, 2, 3]}

d['new_dict'] = {'nested_dict': 1}
print(d)
# To delete an item, delete the key from the dictionary:
del d['newkey']  # deleted 'newkey': 42
print(d)
