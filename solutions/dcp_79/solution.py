def solution(arr):
    n = len(arr)
    count = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if count > 0:
                return False
            if i - 1 >= 0 and arr[i - 1] > arr[i + 1] and i + 2 < n and arr[i] > arr[i + 2]:
                return False
            count += 1
    return True
