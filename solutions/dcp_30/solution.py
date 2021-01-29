def solution(arr):
    n = len(arr)
    if n < 3:
        return 0

    total = 0
    l_max, r_max = arr[0], arr[n-1]
    i, j = 1, n-2
    while i <= j:
        if l_max < r_max:
            total += l_max - arr[i]
            i += 1
        else:
            total += r_max - arr[j]
            j -= 1
        l_max, r_max = max(l_max, arr[i]), max(r_max, arr[j])
    return total


assert solution([1]) == 0
assert solution([2, 1]) == 0
assert solution([2, 1, 2]) == 1
assert solution([4, 1, 2]) == 1
assert solution([4, 1, 2, 3]) == 3
assert solution([10, 9, 1, 1, 6]) == 10
assert solution([3, 0, 1, 3, 0, 5]) == 8
assert solution([3, 4, 1, 5, 0, 3]) == 6
