import random
from typing import List


def process_nums(n: int, nums: List[int]):
    return list(set(num for num in range(0, n)) - set(nums))


def solution(n: int, nums: List[int]):
    new_nums = process_nums(n, nums)
    if len(new_nums) == 0:
        return None
    return random.choice(new_nums)
