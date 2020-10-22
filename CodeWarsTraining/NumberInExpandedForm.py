def expanded_form(num):
    result = []
    divider = 10
    while divider < num:
        temp = num % divider
        if temp != 0:
            result.insert(0, str(temp))
        num -= temp
        divider *= 10
    result.insert(0, str(num))
    return ' + '.join(result)


### OR ###


def expanded_form1(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')


### OR ###


def expanded_form2(num):
    result = []
    for a in range(len(str(num)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(num, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)