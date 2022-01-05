import copy
from typing import List, Dict


def check(start: int, s: str, counter: Dict[str, int], l: int) -> bool:
    if start + l > len(s):
        return False
    for i in range(start, start + l):
        char = s[i]
        if char in counter:
            if char not in counter:
                return False
            counter[char] -= 1
            if counter[char] == 0:
                counter.pop(char)
        else:
            return False
    return len(counter.keys()) == 0


def solution(w: str, s: str) -> List[int]:
    wc = {}
    for c in w:
        if c in wc:
            wc[c] += 1
        else:
            wc[c] = 1
    res = []
    for i, c in enumerate(s):
        if c in wc and check(i, s, copy.deepcopy(wc), len(w)):
            res.append(i)
    return res
