# This example illustrates how the default key is chosen if we do not specify any
import itertools
c = itertools.groupby(['goat', 'dog', 'cow', 1, 1, 2, 3,
                       11, 10, ('persons', 'man', 'woman')])
dic = {}
for k, v in c:
    dic[k] = list(v)
print(dic)

# Results in
# {1: [1, 1],
# 2: [2],
# 3: [3],
# ('persons', 'man', 'woman'): [('persons', 'man', 'woman')],
# 'cow': ['cow'],
# 'dog': ['dog'],
# 10: [10],
# 11: [11],
# 'goat': ['goat']}

# Notice here that the tuple as a whole counts as one key in this list
