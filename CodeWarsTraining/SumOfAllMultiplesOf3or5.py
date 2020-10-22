def find(n):
    sum = 0
    for i in range(n+1):
        if not (i % 3) or not (i % 5):
            sum += i
    return sum


### OR ###


def find1(n):
    return sum(i for i in range(n+1) if not (i % 3) or not (i % 5))


print(find1(10))