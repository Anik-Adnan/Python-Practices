#1234=1+2+3+4=10

sum=0
n=input("enter number :")
for i in range(0,len(n)):
    sum+=int(n[i])
print(f"sum = {sum}")