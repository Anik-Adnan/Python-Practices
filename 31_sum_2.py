#sum of digits
#1234=1+2+3+4 =10
n=input("Enter number :")
i=1
sum=0
while i<=len(n):
    sum+=int(n[i-1])
    i+=1
print(f"sum = {sum}")