# we use enumerate function with for loop to track position of our
# item in iterable

# without enumeratefunction
names = ['abc', 'def', 'anik', 'adnan']
# pos=0
# for name in names:
#     print(f'{pos} ---> {name}')
#     pos+=1

# with enumerate
for pos,name in enumerate(names):
    print(f'{pos} ---> {name}')