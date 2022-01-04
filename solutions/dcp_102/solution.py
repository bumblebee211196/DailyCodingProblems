from typing import List


def solution(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n == 0:
        return []
    curr_sum = start = end = 0
    for i, num in enumerate(nums):
        curr_sum += num
        end = i + 1
        while curr_sum > k:
            curr_sum -= nums[start]
            start += 1
        if curr_sum == k:
            return nums[start:end]
    return []
