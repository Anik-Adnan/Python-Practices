# Retrieving data from a file
# The following snippet opens a JSON encoded file (replace filename with the actual name of the file) and returns the
# object that is stored in the file.
import json
import os

print(os.getcwd())
with open('2_jeson_retring_data.txt', 'w') as f:
    d = json.load(f)
    print(d)
