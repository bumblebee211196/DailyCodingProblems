import sys


def solution(arr):
    if not arr or len(arr) < 2:
        return
    min_price = arr[0]
    res = -sys.maxsize
    for i in range(1, len(arr)):
        res = max(res, arr[i] - min_price)
        min_price = min(min_price, arr[i])
    return res


assert not solution([9])
assert solution([9, 11, 8, 5, 7, 10]) == 5
assert solution([1, 2, 3, 4, 5]) == 4
assert solution([1, 1, 1, 1, 1]) == 0
assert solution([1, 1, 1, 2, 1]) == 1
assert solution([5, 4]) == -1
