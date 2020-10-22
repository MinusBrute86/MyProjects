def basic_op(operator, value1, value2):
    x = str(value1) + str(operator) + str(value2)
    return eval(x)


### OR ###


def basic_op1(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2


### OR ###


def basic_op2(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


### OR ###


def basic_op3(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))


### OR ###


def basic_op4(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')