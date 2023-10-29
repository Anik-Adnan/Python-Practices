name,c = input("Enter your name and chracter : ").split(",")
print(f"name length = {len(name.strip())}")
print(f"character count : {name.strip().lower().count(c.strip().lower())}")
