def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function

    lst = []
    for i in range(a,b+1):
        if i > 9:
            s = sum_dig(i)
            if s == i:
                lst.append(i)
        else:
            lst.append(i)
    return lst


def sum_dig(num):
    n = 1
    tot = 0
    for dig in str(num):
        tot += int(dig)**n
        n+=1
    return tot


### OR ###


def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow1(a, b):
    return filter(filter_func, range(a, b+1))


### OR ###


def sum_dig_pow2(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]


### OR ###


def sum_dig_pow3(a, b): # range(a, b + 1) will be studied by the function
    res = []
    for number in range(a, b+1):
        digits = [int(i) for i in str(number)]
        s = 0
        for idx, val in enumerate(digits):
            s += val ** (idx + 1)
        if s == number:
            res.append(number)
    return res