def solution1(n):
    if n == 1:
        return 1
    if n in (0, 2, 3):
        return 0
    board = [[0] * n for _ in range(n)]
    res = [0]

    def _solution(row=0):
        if row == n:
            res[0] += 1
            return
        for c in range(n):
            if is_valid1(board, row, c):
                board[row][c] = 1
                _solution(row + 1)
                board[row][c] = 0

    _solution()
    return res[0]


def is_valid1(board, r, c):
    for i in range(r):
        if board[i][c] == 1:
            return False
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(r, -1, -1), range(c, len(board))):
        if board[i][j] == 1:
            return False
    return True


assert solution1(0) == 0
assert solution1(2) == 0
assert solution1(4) == 2
assert solution1(8) == 92


def solution2(n, board=[]):
    if n == 0:
        return 0
    if n == len(board):
        return 1
    count = 0
    for c in range(n):
        board.append(c)
        if is_valid2(board):
            count += solution2(n, board)
        board.pop()
    return count


def is_valid2(board):
    r, c = len(board) - 1, board[-1]
    for i, j in enumerate(board[:-1]):
        diff = abs(c - j)
        if diff == 0 or diff == r - i:
            return False
    return True


assert solution2(0) == 0
assert solution2(2) == 0
assert solution2(4) == 2
assert solution2(8) == 92
