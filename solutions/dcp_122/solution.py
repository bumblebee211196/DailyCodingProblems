from typing import List


def solution(matrix: List[List[int]]) -> int:

    rows, cols = len(matrix), len(matrix[0])

    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    dp[1][1] = matrix[0][0]

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            dp[r][c] = matrix[r - 1][c - 1] + max(dp[r - 1][c], dp[r][c - 1])

    return dp[-1][-1]


print(solution([[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]))
