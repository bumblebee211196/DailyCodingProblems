def solution(x, y):
    if y == 1:
        return x
    res = solution(x, y // 2)
    if y % 2 == 0:
        return res * res
    return res * res * x


assert solution(2, 10) == 1024
assert solution(2, 5) == 32
