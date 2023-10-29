#removing space 
#removing left space method lstrip()
n="    anik    Adnan     "
dot="......"
s=n+dot
print(f"before removing spaces       :{n}")
print(f"after removing left   spaces :{n.lstrip()}")
print(f"Without removing  spaces:{s}")
print(f"after removing right spaces :{n.rstrip()+dot}")
#strip removes all spaces right and left
print(f"using strip removing  spaces :{n.strip()+dot}")
#remove all spaces in a string
#use replace("which repalced", "what will bw by replaced") method , 2perameter
print(s.replace(" ", ""))
#print(f"Removing all space :{s.replace(" ", "")}")
print(n.find("k")) #lenght of "k" character
