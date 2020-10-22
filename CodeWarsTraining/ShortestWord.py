def find_short(s):
    l = s.split()   # splits string word by word instead of letter by letter
    return len(min(l, key=len))  # returns length of smallest word in 'l'


### OR ###


def find_short1(s):
    return min(len(l) for l in s.split())