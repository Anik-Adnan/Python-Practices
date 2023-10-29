s = "anika adnan"
pos = 4


def remove_char(s, pos):
    new_str = ""
    for i in range(len(s)):
        if pos != i:
            new_str += s[i]
    return new_str


print(s)
print(remove_char(s, pos))

s = "Anika Biswas"


def remove_char_2(s, pos):
    new_str = s[:pos] + s[pos + 1:]
    return new_str


print(s)
print(remove_char_2(s, pos))

# 333
s = "AAnik"
pos = 0
new_str = ''.join([s[i] for i in range(len(s)) if i != pos])
print(s)
print(new_str)
