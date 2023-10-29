# Storing data in a file
# The following snippet encodes the data stored in d into JSON and stores it in a file (replace filename with the actual
# name of the file).
import json
d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3]
}
with open('jeson_2.txt', 'w') as f:
    json.dump(d, f)
