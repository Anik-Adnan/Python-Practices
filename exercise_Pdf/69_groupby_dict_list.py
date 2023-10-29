# In this example we see what happens when we use different types of iterable.
import itertools
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"),
          ("vehicle", "speed boat"), ("vehicle", "school bus")]
dic = {}
def f(x): return x[0]


for key, group in itertools.groupby(sorted(things, key=f), f):
    dic[key] = list(group)
print(dic)
# Results in
# {'animal': [('animal', 'bear'), ('animal', 'duck')],
# 'plant': [('plant', 'cactus')],
# 'vehicle': [('vehicle', 'harley'),
# ('vehicle', 'speed boat'),
# ('vehicle', 'school bus')]}
