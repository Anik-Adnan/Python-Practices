#list vs string
#string sre immutable(value not changeable in the original variable)
#list are mutable(value changable)
s='anik'
l=s.title()
print(l)
# print(s.lower())
# print(s.upper())
# print(s.count('a'))
# print(s.find('i'))
# print(s.replace('k','t',1))
# print(s.center(len(s)+8,'*'))

print("list")
list=['anik','adnan','20','biswas']
list.pop()#remove list element
print(list)#without biswas
list.append("biswas")#add biswas
print(list)

