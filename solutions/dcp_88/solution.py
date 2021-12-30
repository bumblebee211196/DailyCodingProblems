def solution(x, y):
    if y == 0:
        raise ZeroDivisionError
    if y == 1:
        return x
    q = 0
    while x >= y:
        q += 1
        x -= y
    return q