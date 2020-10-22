from statistics import mode


def stray(arr):
    for num in arr:
        if num != mode(arr):
            return num


### OR ###


def stray1(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x