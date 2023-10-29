user_name= input("Enter your name :")
user_age= int(input("Enter your agge  :"))
if user_age >= 18 and (user_name[0]=='a' or user_name[0]=='A'):
    print("Access granted!!")
else:
    print("Access denied !!")

