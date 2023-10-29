# set comprehension 
# unorder data collection
s = {k**2 for k in range(1,11)}
print(s)

names = ['Anik', 'adnan','biswas']
first = { name[0] for name in names}
print(first)