data = 'chandan purohit 22 2000' 
# assuming data fields of fixed length
name_slice = slice(0,16)
age_slice = slice(16,18)
salary_slice = slice(19,None)
# now we can have more readable slices
print(data[name_slice]) #chandan purohit
print(data[age_slice]) #'22'
print(data[salary_slice]) #'2000'

# __getitem__
print(data.__getitem__(1 )) # data[1] = h