import re


def run(string):

    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in search
    # method of regex object.
    if(regex.search(string) == None):
        print("String is accepted")

    else:
        print("String is not accepted.")


string = "adnananik131032@gmail.com"
run(string)
