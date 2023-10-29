#string palindrome
a=input()
def palindrome(a):
    if a[:]==a[::-1]:
        return "palindrome"
    return "Not palindrome"

# def palindrome(a):
#     return a[:]==a[::-1] #return true or false

print(palindrome(a))
