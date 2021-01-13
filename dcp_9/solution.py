def solution(arr):
    n = len(arr)
    if n == 1:
        return arr[-1]
    if n == 2:
        return max(arr)
    prev2, prev1 = arr[0], max(arr[0], arr[1])
    for i in range(2, n):
        curr = max(prev1, arr[i] + prev2)
        prev2, prev1 = prev1, curr
    return prev1


assert solution([2, 4, 6, 2, 5]) == 13
assert solution([5, 1, 1, 5]) == 10
