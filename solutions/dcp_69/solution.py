from functools import reduce

def product(x, y): return x * y


def solution(numbers):
    numbers = sorted(numbers)
    return max(reduce(product, numbers[:2] + [numbers[-1]]), reduce(product, numbers[-3:]))
