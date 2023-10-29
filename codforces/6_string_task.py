s = input().lower()
vowel = "aoyeui"
new_str = ""
for i in range(len(s)):
    if s[i] not in vowel:
        new_str += "."+s[i]
    elif s[i] in vowel:
        s.replace('i', "")
print(new_str)
