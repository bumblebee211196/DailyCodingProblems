def solution(x, y):
    if y == 0:
        raise ZeroDivisionError
    if y == 1:
        return x
    quotient = temp = 0
    for i in range(31, -1, -1):
        if temp + (y << i) <= x:
            temp += y << i
            quotient |= 1 << i
    return quotient