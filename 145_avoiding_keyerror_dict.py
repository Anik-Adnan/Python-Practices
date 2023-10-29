my_dict = {}
my_dict['key1'] = 'anik'
my_dict['key2'] = 'adnan'
my_dict['key3'] = 'biswas'
# multiples ways
print(my_dict.get('key1', 'not found'))

print(my_dict.setdefault('anik', 'not found anik'))

##
search_key = input('key name: ')
try:
    value = my_dict[search_key]
except KeyError:
    value = 'key not found'
print(value)

##
key = input('input key name: ')
if key in my_dict:
    value = my_dict[key]
else:
    value = 'input key not found'
print(value)
