# ** keyword argument unpacking operator to deliver the key-value pairs in a dictionary into a function's arguments
def parrot(voltage, state, action):
    print("This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


parrot(220, 'city', 'none')
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)
# {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}
# As this example demonstrates, duplicate keys map to their lattermost value(for example "Clifford" overrides "Nemo"
