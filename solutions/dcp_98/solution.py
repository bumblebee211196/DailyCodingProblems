from typing import List, Set, Tuple


def dfs(row: int, col: int, idx: int, board: List[List[str]], word: str, visited: Set[Tuple[int, int]]) -> bool:
    rows, cols, n = len(board), len(board[0]), len(word)
    if idx == len(word):
        return True
    if 0 <= row < rows and 0 <= col < cols and board[row][col] == word[idx] and (row, col) not in visited:
        visited.add((row, col))
        return (
            dfs(row + 1, col, idx + 1, board, word, visited)
            or dfs(row - 1, col, idx + 1, board, word, visited)
            or dfs(row, col + 1, idx + 1, board, word, visited)
            or dfs(row, col - 1, idx + 1, board, word, visited)
        )
    return False


def solution(board: List[List[str]], word: str) -> bool:
    rows, cols, n = len(board), len(board[0]), len(word)
    for row in range(rows):
        for col in range(cols):
            visited = set()
            if n == 1 and board[row][col] == word:
                return True
            if board[row][col] == word[0] and dfs(row, col, 0, board, word, visited):
                return True
    return False
