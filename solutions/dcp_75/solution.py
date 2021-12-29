def get_index(arr, target):
    l, r = 0, len(arr) - 1
    res = r + 1
    while l <= r:
        mid = (l + r) // 2
        if target < arr[mid]:
            res = mid
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1
        else:
            return mid
    return res


def solution(nums):
    if not nums:
        return 0
    dp = []
    res = 0
    for num in nums:
        idx = get_index(dp, num)
        if idx == res:
            dp.append(num)
            res += 1
        else:
            dp[idx] = num
    return res
