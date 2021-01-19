def solution(word1, word2):
    n1, n2 = len(word1), len(word2)
    dp = [[None for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    def _solution(i, j):
        if dp[i][j]:
            return dp[i][j]
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        elif word1[i-1] == word2[j-1]:
            dp[i][j] = _solution(i-1, j-1)
        else:
            dp[i][j] = 1 + min(
                _solution(i-1, j),
                _solution(i, j-1),
                _solution(i-1, j-1),
            )
        return dp[i][j]
    return _solution(n1, n2)


assert solution("", "") == 0
assert solution("a", "b") == 1
assert solution("abc", "") == 3
assert solution("abc", "abc") == 0
assert solution("kitten", "sitting") == 3
