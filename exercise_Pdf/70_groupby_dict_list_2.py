
# The only difference is that I have changed all the
# tuples to lists.
import itertools
things = [["animal", "bear"], ["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"],
          ["vehicle", "speed boat"], ["vehicle", "school bus"]]
dic = {}
def f(x): return x[0]


for key, group in itertools.groupby(sorted(things, key=f), f):
    dic[key] = list(group)
print(dic)

# output
# {'animal': [['animal', 'bear'], ['animal', 'duck']],
# 'plant': [['plant', 'cactus']],
# 'vehicle': [['vehicle', 'harley'],
# ['vehicle', 'speed boat'],
# ['vehicle', 'school bus']]}
# Section 23.2: Example
