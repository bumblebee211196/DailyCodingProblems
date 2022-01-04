def solution(a: str, b: str) -> bool:
    if len(a) == len(b) == 1:
        return True
    if len(a) != len(b):
        return False
    b_dict = {v: i for i, v in enumerate(b)}
    n = len(a)
    for i in range(n):
        al = i - 1
        ar = (i + 1) % n
        bl = b_dict[a[i]] - 1
        br = (b_dict[a[i]] + 1) % n
        if a[al] != b[bl] or a[ar] != b[br]:
            return False
    return True
