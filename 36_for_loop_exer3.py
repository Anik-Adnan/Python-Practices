name=input("entetr your name :")
temp=""
for i in range(0,len(name)):
    if name[i] not in " " and name[i] not in temp:
        temp+=name[i]
        print(f"{temp}")
        print(f"{name[i]} : {name.count(name[i])}")