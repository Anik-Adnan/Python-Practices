# Notice in this example that mulato and camel don't show up in our result. Only the last element with the specified
# key shows up. The last result for c actually wipes out two previous results. But watch the new version where I have
# the data sorted first on same key.
import itertools

list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'),
               'wombat', 'mongoose', 'malloo', 'camel']
c = itertools.groupby(list_things, key=lambda x: x[0])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

# Results in


# Sorted Version
list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'),
               'wombat', 'mongoose', 'malloo', 'camel']
sorted_list = sorted(list_things, key=lambda x: x[0])
print(sorted_list)
print()
c = itertools.groupby(sorted_list, key=lambda x: x[0])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

# Results in
# ['cow', 'cat', 'camel', 'dog', 'donkey', 'goat', 'mulato', 'mongoose', 'malloo', ('persons', 'man', 'woman'), 'wombat']

# {'c': ['cow', 'cat', 'camel'], 'd': ['dog', 'donkey'], 'g': ['goat'],
# 'm': ['mulato', 'mongoose', 'malloo'], 'persons': [('persons', 'man',
# 'woman')], 'w': ['wombat']}
