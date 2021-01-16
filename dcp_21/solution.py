def solution(intervals):
    n = len(intervals)
    if n == 0:
        return 0
    starts = sorted([start for start, _ in intervals])
    ends = sorted([end for _, end in intervals])
    i = j = 0
    rooms = result = 0
    while i < n and j < n:
        if starts[i] < ends[j]:
            rooms += 1
            result = max(result, rooms)
            i += 1
        else:
            rooms -= 1
            j += 1
    return result


assert solution([]) == 0
assert solution([(30, 75), (0, 50), (60, 150)]) == 2
assert solution([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert solution([(60, 150)]) == 1
assert solution([(60, 150), (150, 170)]) == 1
assert solution([(60, 150), (60, 150), (150, 170)]) == 2
