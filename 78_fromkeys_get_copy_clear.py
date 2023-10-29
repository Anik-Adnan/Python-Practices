# fromkeys
# d = {'name' : 'unknown', 'age': 'unknown' }

d = dict.fromkeys( ['name', 'age', 'height' ], 'unknown')
print(d) 

# d = dict.fromkeys( ('name2', 'age2', 'height2' ), 'unknown')
# print(d) 

# d = dict.fromkeys( 'abcd', 'unknown')
# print(d) 
d = dict.fromkeys( (range(1,6) ), 'unknown')
print(d) 

#get method
d = dict.fromkeys( ['name', 'age', 'height' ], 'unknown')
print('get method')
print(d['name']) #print(d['names']) error
print(d.get('age'))
print(d.get('ages')) # not error it gives none 

# if d.get('ages'):
#     print('age  present')
# else:
#     print("not present")

#clear methods
print('clear method')
d.clear()
print(d) #empyty dict. all clear items

#copy method
print('copy method')
d = {'name' : 'unknown', 'age': 'unknown' }

a=d.copy()
print(a)

# a=d means same dictionary, a changed d is changed

