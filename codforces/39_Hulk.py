n = int(input())
odd = "I hate"
add = "that"
even = "I love"
last = "it"
result = ""
for i in range(1, n+1):
    if i % 2 == 1:
        result += odd
    else:
        result += even

    if i == n:
        result += " " + last
    else:
        result += " " + add+" "
print(result)
