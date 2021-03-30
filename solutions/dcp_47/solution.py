def solution(nums):
    if not nums:
        return 0
    prev_min = nums[0]
    profit = 0
    for num in nums:
        profit = max(profit, num - prev_min)
        prev_min = min(prev_min, num)
    return profit


assert solution([9, 11, 8, 5, 7, 10]) == 5
assert solution([9]) == 0
assert solution([9, 11, 8, 5, 7, 10]) == 5
assert solution([1, 2, 3, 4, 5]) == 4
assert solution([1, 1, 1, 1, 1]) == 0
assert solution([1, 1, 1, 2, 1]) == 1
assert solution([5, 4]) == 0
