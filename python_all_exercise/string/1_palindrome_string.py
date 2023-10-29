s = "madam"


def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True


print(is_palindrome(s))
s = "anik"


def is_palindrome_2(s):
    return s == s[::-1]


print(is_palindrome_2(s))
s = "malayalam"


def is_palindrome_3(S):
    rev = "".join(reversed(s))
    if rev == s:
        return True
    return False


print(is_palindrome_3(s))

s = "adnan"


def is_palindrome_4(s):
    ss = ""
    for i in s:
        ss = i+ss
    if s == ss:
        return True
    return False


print(is_palindrome_4(s))
