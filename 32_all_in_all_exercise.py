name= input("Enter your name :")
i=0
temp=""
while i<len(name):
    if name[i] not in temp and name[i] not in " ":
        temp+=name[i]
        print(f" {name[i]}:{name.count(name[i])}")
    i+=1



