import re
s1 = 'anik adnan'
s2 = "asif biswas"


def cout_matching_char(s1, s2):
    count = 0
    j = 0
    for i in s1:
        if s2.find(i) >= 0 and j == s1.find(i) and i != " ":
            count += 1
        j += 1
    print("number of matching charecter is ", count)


cout_matching_char(s1, s2)


def cout_matching_char_2(s1, s2):
    s1 = set(s1.replace(" ", ""))
    s2 = set(s2.replace(" ", ""))
    res = s1 & s2
    print("number of matching charecter is ", len(res))


cout_matching_char_2(s1, s2)
