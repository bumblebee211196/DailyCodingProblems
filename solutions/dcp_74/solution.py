import math


def solution(n, x):
    res = 0
    for i in range(1, x + 1):
        if x % i == 0 and (x // i <= n and i <= n):
            res += 1
    return res
