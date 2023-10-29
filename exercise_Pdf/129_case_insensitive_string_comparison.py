# help(str.casefold)
# Do not just use lower. If casefold is not available, doing .upper().lower() helps (but only somewhat).
# Then you should consider accents. If your font renderer is good, you probably think "ê" == "ê" - but it doesn't:
# >>> "ê" == "ê"
# False

# This is because they are actually
import unicodedata
print([unicodedata.name(char) for char in "ê"])
# ['LATIN SMALL LETTER E WITH CIRCUMFLEX']
print([unicodedata.name(char) for char in "ê"])
# ['LATIN SMALL LETTER E', 'COMBINING CIRCUMFLEX ACCENT']


# The simplest way to deal with this is unicodedata.normalize. You probably want to use NFKD normalization, but
# feel free to check the documentation. Then one does
# >> > unicodedata.normalize("NFKD", "ê") == unicodedata.normalize("NFKD", "ê")
# True

# To finish up, here this is expressed in functions:


def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())


def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)
