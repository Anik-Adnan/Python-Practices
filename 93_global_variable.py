x = 'Hi' # x is global
# x is just referenced, therefore assumed global
def read_x():
    print(x)  
read_x() # prints Hi
def read_y():
    y = 'anik' # y appears in an assignment, therefore it's local
    print(y) # will find the local y
read_y() # prints Hey
# print(y) # error 

a = 'hello Anik Adnan'
def change_global_x():
    global a 
    print(a)
    a = 'Bye'
   
change_global_x() # prints Bye
print(a) # prints Bye