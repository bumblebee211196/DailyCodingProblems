# 0 is unvisited
# 1 is visited


def solution(n):
    res = 0
    for r in range(n):
        for c in range(n):
            board = [[0 for _ in range(n)] for _ in range(n)]
            board[r][c] = 1
            res += search(board, n, [(r, c)])
    return res


def get_candidates(r, c, board, n):
    for x, y in [
        (r - 1, c + 2),
        (r + 1, c + 2),
        (r - 1, c - 2),
        (r + 1, c - 2),
        (r + 2, c + 1),
        (r + 2, c - 1),
        (r - 2, c + 1),
        (r - 2, c - 1),
    ]:
        if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
            yield (x, y)


def search(board, n, tour):
    if len(tour) == n * n:
        return 1
    res = 0
    r, c = tour[-1]
    for x, y in get_candidates(r, c, board, n):
        board[x][y] = 1
        tour.append((x, y))
        res += search(board, n, tour)
        board[x][y] = 0
        tour.pop()
    return res
