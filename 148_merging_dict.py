from itertools import chain
from collections import ChainMap
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

# dict uses the latter dict to overwrite the previous one.
fish_dog = {**fish, **dog}
print(fish_dog)
print(dict(chain(fish.items(), dog.items())))
fish.update(dog)
print(fish)
# {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}


fish_dog = {**dog, **fish}
print(fish_dog)
print(dict(ChainMap(fish, dog)))
# {'name': 'Nemo', 'hands': 'fins', 'color': 'red', 'special': 'gills'}
