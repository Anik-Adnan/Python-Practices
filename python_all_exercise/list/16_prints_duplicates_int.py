def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(0, size):
        for j in range(i+1, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(Repeat(list1))
l = "anik adnan"
print(Repeat(l))
