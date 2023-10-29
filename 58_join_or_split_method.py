#split method
#conveting string to list
user_info="anik adnan 24".split()  
print(user_info)
user_info="anik adnan, 24".split(",")  
print(user_info)

name,age="anik adnan,24".split(",")  
print(name)
print(age)
nam, ag = input("name and age: ").split(',')  
print(f"name : {nam} and age is : {ag}")

#join method
#converting list to string
print("join method")
user=['anik','adnan','20']
print(','.join(user))
