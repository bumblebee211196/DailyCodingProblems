def solution(arr):
    res = [[]]
    for i, v in enumerate(arr):
        temp = []
        while len(res) > 0:
            ele = res.pop(0)
            temp.append(ele)
            temp.append(ele + [v])
        res = temp
    return res


assert solution([]) == [[]]
assert solution([1]) == [[], [1]]
assert solution([1, 2]) == [[], [2], [1], [1, 2]]
assert solution([1, 2, 3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
assert solution([1, 2, 3, 4]) == [
    [],
    [4],
    [3],
    [3, 4],
    [2],
    [2, 4],
    [2, 3],
    [2, 3, 4],
    [1],
    [1, 4],
    [1, 3],
    [1, 3, 4],
    [1, 2],
    [1, 2, 4],
    [1, 2, 3],
    [1, 2, 3, 4],
]
