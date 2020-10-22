import string


def ispangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False
    return True


### OR ###


def is_pangram1(s):
    return set(string.lowercase) <= set(s.lower())


### OR ###


