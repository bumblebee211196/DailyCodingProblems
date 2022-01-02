from typing import List


def solution(nums: List[int]) -> List[int]:
    def helper(arr, res):
        if not arr:
            result.append(res[:])
            return
        for val in arr:
            temp = arr.copy()
            temp.remove(val)
            res.append(val)
            helper(temp, res)
            res.pop()

    result = []
    helper(nums, [])
    return result
