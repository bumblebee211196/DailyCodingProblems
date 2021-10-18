def solution(nums):

    def helper(idx, total):
        if idx == len(nums):
            return total == target
        return helper(idx + 1, total + nums[idx]) or helper(idx + 1, total)
    
    target = sum(nums) // 2
    return helper(0, 0)


print(solution([15, 5, 20, 10, 35, 15, 10]))
print(solution([15, 5, 20, 10, 35]))
