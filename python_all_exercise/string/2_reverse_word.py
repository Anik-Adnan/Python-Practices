sentence = "i am anik adnan"


def rev_sentence(sentence):
    words = sentence.split()
    reverse_sentence = " ".join(reversed(words))
    return reverse_sentence


print(sentence)
print(rev_sentence(sentence))
