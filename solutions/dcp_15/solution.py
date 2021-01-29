import random


def solution(big_stream):
    result = None
    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            result = e
    return result
