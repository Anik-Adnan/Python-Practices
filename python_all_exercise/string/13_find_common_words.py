

def uncommon(a, b):
    list_a = a.split()
    list_b = b.split()
    uc = ''
    for i in list_a:
        if i not in list_b:
            uc = uc+" "+i
    for j in list_b:
        if j not in list_a:
            uc = uc+" "+j

    return uc


# Driver code
a = "apple banana mango"
b = "banana fruits mango"
print(uncommon(a, b))


def uncommon(a, b):
    a = a.split()
    b = b.split()
    k = set(a).symmetric_difference(set(b))
    return k


# Driver code
if __name__ == "__main__":
    a = "apple banana mango"
    b = "banana fruits mango"
    print(list(uncommon(a, b)))


# Python3 program to find a list of uncommon words

# Function to return all uncommon words
def UncommonWords(A, B):

    # count will contain all the word counts
    count = {}

    # insert words of string A to hash
    for word in A.split():
        count[word] = count.get(word, 0) + 1

    # insert words of string B to hash
    for word in B.split():
        count[word] = count.get(word, 0) + 1

    # return required list of words
    return [word for word in count if count[word] == 1]


# Driver Code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

# Print required answer
print(UncommonWords(A, B))


# 4444
def uncommon(A, B):
    un_comm = [i for i in "".join(B).split() if i not in "".join(A).split()]
    return un_comm


# Driver code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
print(uncommon(A, B))
