def solution(code_str):
    if len(code_str) == 1:
        return 1
    n = len(code_str)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if code_str[0] != "0" else 0
    for i in range(1, n):
        if code_str[i] != "0":
            dp[i + 1] += dp[i]
        if code_str[i - 1] != "0" and 10 <= int(code_str[i - 1 : i + 1]) <= 26:
            dp[i + 1] += dp[i - 1]
    return dp[n]


assert solution("111") == 3
assert solution("12345") == 3
assert solution("11111") == 8
