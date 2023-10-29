import math
#trunc() removes floating part
#ceil() print upper int number
#floor() print lower int number
a = float(input("enter a float number :"))
print(f"your number = {a}")
print(f"your number = {math.trunc(a)}")
print(f"your number = {math.ceil(a)}")
print(f"your number = {math.floor(a)}")
print(f"your number = {round(a,2)}")

print(f"your number = {round(a,4)}")
#one problem here if input num lessthan 4 point after decimal point


# using "%" to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using %) is : ",end="") 
print ('%.2f'%a) 
  
# using format() to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using format()) is : ",end="") 
print ("{0:.2f}".format(a)) 
  
# using round() to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using round()) is : ",end="") 
print (round(a,2)) 