def solution(arr):
    i = j = 0
    n = len(arr)
    while j < n:
        if arr[j] > 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    n = i + 1
    for i in range(n):
        if arr[i] < n:
            key = abs(arr[i]) - 1
            if arr[key] > 0:
                arr[key] = -arr[key]
    for i in range(n):
        if arr[i] > 0:
            return i + 1
    return n


assert solution([3, 4, -1, 1]) == 2
assert solution([1, 2, 0]) == 3
assert solution([-5, 7, -3, -4, 9, 10, -1, 11]) == 1
