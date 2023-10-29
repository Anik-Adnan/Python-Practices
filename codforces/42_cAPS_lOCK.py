s = input()
up_count = 0
for i in range(len(s)):
    if s[i].isupper():
        up_count += 1

if up_count == len(s):
    print(s.lower())
elif s[0].islower() == True and up_count == len(s) - 1:
    print(s.title())
else:
    print(s)
