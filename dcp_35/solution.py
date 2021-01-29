def solution(arr):
    n = len(arr)
    if n in (0, 1):
        return arr
    l, m, h = 0, 1, n-1
    while m <= h:
        if arr[m] == 'R':
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 'G':
            m += 1
        else:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    return arr


assert solution(['G', 'R']) == ['R', 'G']
assert solution(['G', 'B', 'R']) == ['R', 'G', 'B']
assert solution(['B', 'G', 'R']) == ['R', 'G', 'B']
assert solution(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
