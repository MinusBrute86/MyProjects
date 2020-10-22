def delete_nth(order, max_e):
    list = []   # Get a new list that we will return
    occurrences = {}  # Get a dictionary to count the occurrences
    for n in order:  # Loop through all provided numbers
        count = occurrences.setdefault(n, 0)  # Get the count of the current number, or assign it to 0
        if count >= max_e:  # If we reached the max occurrences for that number, skip it
            continue
        list.append(n)  # Add the current number to the list
        occurrences[n] += 1  # Increase the occurrences n++
    return list  # We are done, return the list


### OR ###


def delete_nth1(order, max_e):
    list = []
    for n in order:
        if list.count(n) < max_e:
            list.append(n)
    return list


### OR ###


def delete_nth2(order, max_e):
    answer = []
    for x in order:
        if answer.count(x) < max_e:
            answer.append(x)
    return answer