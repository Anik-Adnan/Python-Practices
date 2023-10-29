#common method to deete data from list
#pop method
name=['anik','adnan','anik','adnan','biswas']
name.pop()#without argument defaule delete last element
print(name)
#pop method with argument delete argument position element
name=['anik','adnan','biswas']
name.pop(2)
print(name)

#del operator
name=['anik','adnan','biswas']
del name[2]
print(name)

#remove method
#delete select element 
#remove first matching element
name=['anik','adnan','biswas']
name.remove("adnan")
print(name)

#remove first matching element
name=['anik','adnan','biswas','adnan']
name.remove("adnan")
print(name)



