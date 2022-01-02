from typing import List, Tuple


def get_distance(start: Tuple[int, int], end: Tuple[int, int]) -> int:
    dist1 = min(abs(start[0] - end[0]), abs(start[1] - end[1]))
    dist2 = max(abs(start[0] - end[0]), abs(start[1] - end[1])) - dist1
    return dist1 + dist2


def solution(points: List[Tuple[int, int]]) -> int:
    start = points[0]
    dist = 0
    for end in points[1:]:
        dist += get_distance(start, end)
        start = end
    return dist
