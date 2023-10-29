#input a name and a character 
#output length of name and count character (char count insensitive)
name,c = input("Enter your name and chracter : ").split(",")
print(f"name length = {len(name)}")
#name lower/capital and char. lower/capital andthen compare andthan count
print(name.lower().count(c.lower()))
