def solution(nums):
    cmax = gmax = 0
    for num in nums:
        cmax = max(num, cmax + num)
        gmax = max(gmax, cmax)
    return gmax


assert solution([34, -50, 42, 14, -5, 86]) == 137
assert solution([-5, -1, -8, -9]) == 0
assert solution([44, -5, 42, 14, -150, 86]) == 95
