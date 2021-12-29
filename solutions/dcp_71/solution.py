from random import randint

def rand7():
    return randint(1, 7)


def rand5():
    value = rand7()
    if value > 5:
        return rand5()
    return value