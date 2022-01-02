def solution(arr, target):
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        if arr[m] >= arr[l]:
            if arr[l] <= target < arr[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if arr[m] < target <= arr[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


assert solution([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert solution([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert solution([1], 0) == -1
