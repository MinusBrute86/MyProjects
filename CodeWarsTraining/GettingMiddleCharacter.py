def get_middle(s):
    return s[(len(s)-1)//2:(len(s)+2)//2]


### OR ###


def get_middle1(s):
    while len(s) > 2:
        s = s[1:-1]
    return s


print(get_middle1("middle"))