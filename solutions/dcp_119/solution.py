from typing import List, Set


def intersecting(x1, y1, x2, y2):
    return not (y1 < x2 or y2 < x1)


def solution(intervals: List[List[int]]) -> Set[int]:
    res = set()
    if not intervals:
        return res
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    n = len(intervals)
    i = 0
    while i < n:
        x1, y1 = intervals[i]
        while i < n and intersecting(x1, y1, *intervals[i]):
            x1, y1 = max(x1, intervals[i][0]), min(y1, intervals[i][1])
            i += 1
        res.add(y1)
    return res


print(solution([[0, 3], [2, 6], [3, 4], [6, 9]]))
