def solution(matrix):
    def is_valid(i, j, v):
        # Check column
        for c in range(N):
            if c != j and matrix[i][c] == v:
                return False
        # Check row
        for r in range(N):
            if r != i and matrix[r][j] == v:
                return False
        # Check 3 X 3 matrix
        rs, cs = (i // 3) * 3, (j // 3) * 3
        for r in range(rs, rs + 3):
            for c in range(cs, cs + 3):
                if r != i and c != j and matrix[r][c] == v:
                    return False
        return True

    def solve():
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 0:
                    for v in range(1, 10):
                        if is_valid(i, j, v):
                            matrix[i][j] = v
                            if solve():
                                return True
                            else:
                                matrix[i][j] = 0
                    return False
        return True

    N = 9
    solve()
    return matrix


assert solution(
    [
        [0, 2, 0, 5, 0, 1, 0, 9, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 6],
        [0, 3, 0, 0, 6, 0, 0, 7, 0],
        [0, 0, 1, 0, 0, 0, 6, 0, 0],
        [5, 4, 0, 0, 0, 0, 0, 1, 9],
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [0, 9, 0, 0, 3, 0, 0, 8, 0],
        [2, 0, 0, 8, 0, 4, 0, 0, 7],
        [0, 1, 0, 9, 0, 7, 0, 6, 0],
    ]
) == [
    [4, 2, 6, 5, 7, 1, 3, 9, 8],
    [8, 5, 7, 2, 9, 3, 1, 4, 6],
    [1, 3, 9, 4, 6, 8, 2, 7, 5],
    [9, 7, 1, 3, 8, 5, 6, 2, 4],
    [5, 4, 3, 7, 2, 6, 8, 1, 9],
    [6, 8, 2, 1, 4, 9, 7, 5, 3],
    [7, 9, 4, 6, 3, 2, 5, 8, 1],
    [2, 6, 5, 8, 1, 4, 9, 3, 7],
    [3, 1, 8, 9, 5, 7, 4, 6, 2],
]

assert solution(
    [
        [0, 1, 0, 0, 0, 0, 8, 0, 9],
        [0, 0, 0, 0, 8, 2, 0, 0, 0],
        [0, 0, 4, 1, 0, 9, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 6, 7, 0, 4, 0, 9, 3, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 3, 0, 1, 6, 0, 0],
        [0, 0, 0, 5, 7, 0, 0, 0, 0],
        [7, 0, 6, 0, 0, 0, 0, 2, 0],
    ]
) == [
    [2, 1, 3, 6, 5, 7, 8, 4, 9],
    [6, 7, 9, 4, 8, 2, 5, 1, 3],
    [5, 8, 4, 1, 3, 9, 2, 7, 6],
    [1, 4, 2, 9, 6, 3, 7, 5, 8],
    [8, 6, 7, 2, 4, 5, 9, 3, 1],
    [3, 9, 5, 7, 1, 8, 4, 6, 2],
    [4, 5, 8, 3, 2, 1, 6, 9, 7],
    [9, 2, 1, 5, 7, 6, 3, 8, 4],
    [7, 3, 6, 8, 9, 4, 1, 2, 5],
]
