for i in range(1,11):
    
    print(f"{i}")
    if i==5:
        break
print("Print odd between 1 - 10 ")
for i in range(1,11):
    if i%2==0:
        print(f"{i}")
    else :
        continue

print("print without 5 between 1- 10 ")
for i in range(1,11):
      
    if i==5:
        continue
    print(f"{i}")
