def solution(n, X=[1, 2]):
    if n in (0, 1):
        return n
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in X:
            if i - j >= 0:
                dp[i] += dp[i - j]
    return dp[-1]


assert solution(4) == 5
assert solution(5) == 8
assert solution(5, [1, 3, 5]) == 5
