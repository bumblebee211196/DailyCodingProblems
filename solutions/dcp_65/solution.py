def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    i = j = 0
    
    while i < rows and j < cols:
        for c in range(j, cols):
            print(matrix[i][c])
        i += 1

        for r in range(i, rows):
            print(matrix[r][cols - 1])
        cols -= 1

        if (i < rows):
            for c in range(cols - 1, j - 1, -1):
                print(matrix[rows - 1][c])
            rows -= 1
        
        if (j < cols):
            for r in range(rows - 1, i - 1, -1):
                print(matrix[r][j])
            j += 1
