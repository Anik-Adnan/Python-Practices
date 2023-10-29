# set data type 
# unordered collection of unique items

a = {1,2,5,2}
print(a)
 # removing list dupticate iteams
b = [1,2,3,4,5,5,4,5,7,9,8,7,10]
print(list(set(b)))
# add,remove, discard ,clear ,copy  method
a.add(10)
a.remove(2) #if element not in a set., showing error
a.discard(2) # if not in set , donot showing error
b=a.copy()
print(b)
print(b.clear())
print(a)
# update method
a.update({10,15})
print(a)