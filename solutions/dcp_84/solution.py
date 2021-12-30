from typing import List

LAND = 1
WATER = 0


def solution(grid: List[List[int]]) -> int:
    
    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == LAND:
            grid[r][c] = WATER
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == LAND:
                islands += 1
                dfs(r, c)
    return islands
