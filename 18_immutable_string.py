#string are immutable
s="anik"
print(s[1])
# a[1]='t' error but repalced valid
print(s.replace("n","t"))
print(s) #not replaced string it's print real string
restring=s.replace("n","t")
print(restring)
