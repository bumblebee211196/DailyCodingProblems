def is_valid_state(board):
    for row in board:
        if 1 in row:
            return False
    return True


def get_candidates(board, x, y):
    rows = cols = len(board)
    candidates = []
    # Check URD
    r, c = x - 1, y + 1
    while r >= 0 and c < cols:
        if (board[r][c] == 1):
            candidates.append((r, c))
        r -= 1
        c += 1
    # Check ULD
    r, c = x - 1, y - 1
    while r >= 0 and c >= 0:
        if (board[r][c] == 1):
            candidates.append((r, c))
        r -= 1
        c -= 1
    # Check LLD
    r, c = x + 1, y - 1
    while r < rows and c >= 0:
        if (board[r][c] == 1):
            candidates.append((r, c))
        r += 1
        c -= 1
    # Check LRD
    r, c = x + 1, y + 1
    while r < rows and c < cols:
        if (board[r][c] == 1):
            candidates.append((r, c))
        r += 1
        c += 1
    return candidates


def search(board, result, x, y):
    if is_valid_state(board):
        return result
    board[x][y] = -1
    for r, c in get_candidates(board, x, y):
        result[0] += 1
        search(board, result, r, c)


def solution(m, bishops):
    board = [[0 for _ in range(m)] for _ in range(m)]
    for r, c in bishops:
        board[r][c] = 1
    result = [0]
    search(board, result, bishops[0][0], bishops[0][1])
    return result[0]
