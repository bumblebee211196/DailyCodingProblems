from typing import List


def solution(arr: List[int], k: int) -> None:
    if not arr:
        return
    n = len(arr)
    k = k % n
    l, m, r = 0, n - k - 1, n - 1
    arr = reverse(l, r, arr)
    arr = reverse(l, m, arr)
    arr = reverse(m + 1, r, arr)


def reverse(l: int, r: int, arr: List[int]) -> List[int]:
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr
