# word counter

def word_counter(s):
    count={}
    for char in s:
        if char not in ' ':
            count[char]= s.count(char)
    return count

print(word_counter("anik adnan"))
    