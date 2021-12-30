def solution(intervals):
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    result = []
    x, y = intervals[0]
    i = 0
    while i < len(intervals):
        x_, y_ = intervals[i]
        if x_ < y and y_ < y:
            i += 1
            continue
        if x_ < y:
            y = y_
        else:
            result.append((x, y))
            x, y = x_, y_
        i += 1
    result.append((x, y))
    return result