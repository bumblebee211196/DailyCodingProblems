def solution(n, m):
    if 0 in (n, m):
        return 0
    if n == m == 1:
        return 1
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        matrix[i][0] = 1
    for j in range(1, m):
        matrix[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[-1][-1]


assert solution(1, 1) == 1
assert solution(2, 2) == 2
assert solution(5, 5) == 70
