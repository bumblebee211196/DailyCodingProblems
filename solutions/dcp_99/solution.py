from typing import List


def solution(nums: List[int]) -> int:
    seen = {}
    res = 1
    for num in nums:
        if num in seen:
            continue
        l = r = num
        if num - 1 in seen:
            l = seen[num - 1][0]
        if num + 1 in seen:
            r = seen[num + 1][1]
        seen[num] = (l, r)
        res = max(res, r - l + 1)
    return res
