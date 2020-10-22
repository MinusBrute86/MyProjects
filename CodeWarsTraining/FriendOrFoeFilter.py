def friend(x):
    list = []   # Initialize list variable
    for name in range(len(x)):  # Loop through list of names
        if len(x[name]) == 4:   # Check to see if the name is of length 4
            list.append(x[name])    # If the name is 4 characters long, append it to variable list
    return list  # Return list


### OR ###


def friend1(x):
    return [i for i in x if len(i) == 4]    # x: list of strings/people
    # returns: list of people with only 4 letters in their names