mydict = {}
# mydict['not there'] # error
# avoiding error use get method
print(mydict.get('key_name', 'not found'))
print(mydict)  # {}
# mydict = {'key': 10}
print(mydict.setdefault('key', 'set_FOUND'))
print(mydict)  # {'key': 'NOT FOUND'}

# another way
try:
    value = mydict['key2']
except KeyError:
    value = 'not_found'

print(value)  # not_found

# another way
if 'key5' in mydict:
    value = mydict['key']
else:
    value = 'not found in dict'
print(value)
