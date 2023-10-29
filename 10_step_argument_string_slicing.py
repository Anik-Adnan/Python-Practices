#syntax [start argumrnt : stopb argument -1  : step]
print("Anik Adnan"[5:10])
print("Adnan"[0: 5 : 1]) #step 1means 1char. after after print
print("Adnan"[0:5 :2])
print("AnikAdnan"[0:10 : 3])
a="adnan"
print(a[1:-1]) # stop argument[-1-1]='a'
print(a[2: : -1]) #[2] to [0]
print(a[-1: : -1])  #[-1]='n' to [0]
print(a[-4: ])
print(a[ : : -1]) #reverce trick
print(a[-1: : ]) 