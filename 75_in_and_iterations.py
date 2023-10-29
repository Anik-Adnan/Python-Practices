# ckeck if key exit in dictionary
user_info={
    'name': "anik adnan",
    'age' : 20
}
if 'name' in user_info:
    print('present')
else :
    print('not present')

#check values
if '20' in user_info.values():
    print('present')
else :
    print('not present')

#loops in dictionary
for i in user_info:
    print(i) #print keys

for i in user_info.values():
    print(i) #print all values

# values() method
print('values method')
user_info_values= user_info.values()
print(user_info)
print(user_info_values)
print(type(user_info_values))

#keys() method
print('key method')
user_info_keys= user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

#print keys values
print('keys all values')
for i in user_info:
    print(user_info[i])

#items method
print('item method')
user_items= user_info.items()
print(user_items)
print(type(user_items))

# print all keys and items
print('all keys and items')
for key,item in user_info.items():
    print(f'key is {key} and item is {item}')