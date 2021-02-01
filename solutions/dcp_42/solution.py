def solution(arr, k, res=None):
    if not res:
        res = []
    if k == 0:
        return [res[:]]
    if not arr or k < 0:
        return []
    for i, v in enumerate(arr):
        res.append(v)
        if solution(arr[i+1:], k-v, res):
            return res
        res.pop()
    return False


assert solution([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]
assert solution([12, 6, 61, 5, 1, 2], 24) == [12, 6, 5, 1]
assert not solution([], 1)
assert solution([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]
assert solution([12, 1, 61, 5, 9, 2], 61) == [61]
