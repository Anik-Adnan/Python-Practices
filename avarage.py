#input 3 numbersbr separating comma and show avarage through string
a,b,c=input("enter a,b,c :").split(",")
print(f"a={a} b={b} c={c}")
sum=int(a)+int(b)+int(c)
print(sum)
avg=float(sum/3)
print(avg)