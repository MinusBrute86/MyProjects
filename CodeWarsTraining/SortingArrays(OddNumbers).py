def sort_array(source_array):
    odd_int = sorted([n for n in source_array if n%2 != 0])
    c = 0
    res = []

    for i in source_array:
        if i %2 != 0:
            res.append(odd_int[c])
            c += 1
        else:
            res.append(i)
    return res


### OR ###


def sort_array1(arr):
    odds = sorted((x for x in arr if x%2 != 0), reverse=True)
    # generator = (x for x in arr if x % 2 != 0), This is a generator to get the odds in arr
    # odds = sorted(generator, reverse = True), sort the result of generator from big to small, store it in odds
    # The usage of reverse is very, very brilliant. You’ll see in the following

    return [x if x%2==0 else odds.pop() for x in arr]
    # This is a combination of list comprehension and conditional expression
    # conditional expression part is ‘ x if x % 2 == 0 else odds.pop()
    # list comprehension part is ‘x for x in arr’

    # this statement equals to :
    # for x in arr:
    #    if x % 2 == 0:
    #        return x
    #    else:
    #        return odds.pop()

    # odds.pop() will delete the last item in list odds and give a return value of the deleted item
    # >>>[1, 2, 3].pop()
    #   3

    # Do you remember the ‘sorted(generator, reverse = True)’? By using odds.pop(), you can get the item in odds from last to first.
    # THAT’S why sets reverse = True.


### OR ###


def sort_array2(source_array):

    odds = []
    answer = []

    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")

        else:
            answer.append(i)

    odds.sort()

    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer