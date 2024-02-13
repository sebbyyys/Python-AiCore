def is_palindrome(input):
    regular = input
    reverse = regular[::-1]

    if regular == reverse:
        return True    
    else:
        return False

is_palindrome("cac")

##same as before just without capitalisation and punctuation

import string
punctuation = string.punctuation


def is_palindrome_check(input):
    regular = ""
    for x in input:
        if x not in punctuation:
            regular += x
    reverse = regular[::-1]

    if regular == reverse:
        return True    
    else:
        return False

#is_palindrome_check("cacl$")
