from heapq import heappop, heappush

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(mat, src, dst):
    m, n = len(mat), len(mat[0])
    x, y = src
    if mat[x][y] == "t":
        return -1
    h = [(0, 0, x, y)]
    visited = set()
    heuristic = lambda i, j: max(m - i - 1, n - j - 1)
    while h:
        heuristic_val, dist, x, y = heappop(h)
        if (x, y) == dst:
            return dist
        for x_, y_ in DIRECTIONS:
            nx, ny = x + x_, y + y_
            if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == "f" and (nx, ny) not in visited:
                visited.add((nx, ny))
                heappush(h, (dist + 1 + heuristic(nx, ny), dist + 1, nx, ny))


matrix = [["f", "f", "f", "f"], ["t", "t", "f", "t"], ["f", "f", "f", "f"], ["f", "f", "f", "f"]]
assert solution(matrix, (0, 0), (0, 0)) == 0
assert solution(matrix, (1, 0), (0, 0)) == -1
assert solution(matrix, (3, 0), (0, 0)) == 7
assert solution(matrix, (3, 0), (0, 3)) == 6

matrix = [["f", "f", "f", "f"], ["t", "t", "t", "f"], ["f", "f", "f", "f"], ["f", "f", "f", "f"]]
assert solution(matrix, (0, 0), (0, 0)) == 0
assert solution(matrix, (1, 0), (0, 0)) == -1
assert solution(matrix, (3, 0), (0, 0)) == 9
assert solution(matrix, (3, 0), (0, 3)) == 6
assert solution(matrix, (2, 0), (3, 3)) == 4
