#looping in tuple
mixed = (1,2,3,4.5)
#for loop in tuple
# for i in mixed:
#     print(i)

#while loop
# i=0
# while i < len(mixed):
#     print(mixed[i])
#     i+=1

# #tauple with one element
# n= (1,) #must inclue a comma fter value
# print(type(n))

# # #tuple without parentheis 
# nam= 'anik', 'adnan' ,'biswas'
# print(type(nam))

# #tuple unpacking
# nam= 'anik', 'adnan' ,'biswas'
# a,b,c= (nam)
# print(a)
# print(b)

# #list inside tuple
# nam= ('anik', ['adnan' ,'biswas'])
# nam[1].append('antor')
# print(nam)

# some function that you can use with tuple
#min(),max(),sum(),len()
nam= (10,50,30)
print(f'max= {max(nam)}  min = {min(nam)} sum = {sum(nam)}')