def solution(arr, k):
    if not arr or k < 1:
        return []
    result = []
    dq = []
    for i, num in enumerate(arr):
        # Pop index, if it is not part of the window
        if dq and dq[0] < i - k + 1:
            dq.pop(0)
        # Pop index, if its value at that index is smaller than element we are looking at, because for the current
        # window, the current element is the maximum
        while dq and arr[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        # Once, i crosses k, we can append value at dq's first index.
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result


assert solution([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert solution([5, 2, 1], 2) == [5, 2]
