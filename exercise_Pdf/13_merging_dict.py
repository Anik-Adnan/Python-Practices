from itertools import chain
from collections import ChainMap
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

# duplicate keys map to their lattermost value (for example "Clifford" overrides "Nemo").
fishdog = {**fish, **dog}
print(fishdog)
# {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}


print(dict(chain(fish.items(), dog.items())))
# {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}
# This uses the lattermost value,


print(dict(ChainMap(fish, dog)))
# {'name': 'Nemo', 'hands': 'fins', 'color': 'red', 'special': 'gills'}
# With this technique the foremost value takes precedence for a given key rather than the last ("Clifford" is thrown out in favor of "Nemo").

fish.update(dog)
print(fish)
# {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}
# dict.update uses the latter dict to overwrite the previous one.
