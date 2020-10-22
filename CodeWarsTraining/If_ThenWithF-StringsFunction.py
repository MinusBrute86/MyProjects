def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return " and ".join(names) + " like this"
    elif len(names) == 3:
        return ", ".join(names[0:2]) + f" and {str(names[-1])} like this"
    else:
        return ", ".join(names[0:2]) + f" and {str(len(names)-2)} others like this"


### OR ###


def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


### OR ###


def likes3(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)


### OR ###


def likes4(names):
    l = len(names)
    if l == 0: return 'no one likes this'
    if l == 1: return '{} likes this'.format(names[0])
    if l == 2: return '{} and {} like this'.format(names[0], names[1])
    if l == 3: return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    return '{}, {} and {} others like this'.format(names[0], names[1], len(names)-2)


print(likes2(["Peter", "Lacy", "Tim", "Sarah", "Blanche"]))