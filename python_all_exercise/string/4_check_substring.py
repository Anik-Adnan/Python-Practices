import re
s = "i am a student"
substr = "student"


def check_substring(s, substr):
    if substr in s:
        return "yes"
    return "no"


print(check_substring(s, substr))
substr = "was"


def check_substring(s, substr):
    if s.find(substr) == 0:
        return "yes"
    return "no"


print(check_substring(s, substr))


def check(s2, s1):
    if (s2.count(s1) > 0):
        print("YES")
    else:
        print("NO")


s2 = "my name is Anik Adnan"
s1 = "name"
check(s2, s1)

if re.search(s1, s2):
    print(s1, " is present")
else:
    print(s1, " is not present")
