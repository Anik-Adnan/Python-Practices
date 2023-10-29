#data structures
#order collection of items
#i can store anything in list int,float,string
number=[1,2,3]
word=["anik",'adnan','name']
mix=[1,2,"three",'four',5.5,6.5,None]
print(number)
print(word)
print(mix)
#accessing list element 
#slicing allowed
print(number[1])
print(mix[4])
print(mix[2: 5])
print(word[1])
print(word[:: -1])
#changed list value
number[2]=100 #before number[2]was 3 but now it's 100
print(number)
#replaced allowed
number[1:]='two'
print(number)
number[1:]=['two','three','four']
print(number)


