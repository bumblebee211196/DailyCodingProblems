from typing import Tuple


def solution(n: int) -> Tuple[int, int]:
    sieve = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    primes = [i for i in range(n + 1) if i > 1 and sieve[i]]
    seen = {}
    for p in primes:
        if abs(n - p) in seen or p == abs(n - p):
            return p, n - p
        seen[p] = True
