def solution(letters):
    rows, cols = len(letters), len(letters[0])
    if rows in (0, 1):
        return 0
    cols_to_be_removed = set()
    letters = [[letters[j][i] for j in range(rows)] for i in range(cols)]
    for i in range(cols):
        col = letters[i]
        r_start = 0
        for r_end in range(1, rows):
            if col[r_start] > col[r_end]:
                cols_to_be_removed.add(i)
                break
            r_start += 1
    return len(cols_to_be_removed)


solution(
    [
        ["c", "b", "a"],
        ["d", "a", "f"],
        ["g", "h", "i"],
    ]
)
solution([["a", "b", "c", "d", "e", "f"]])
solution(
    [
        ["z", "y", "x"],
        ["w", "v", "u"],
        ["t", "s", "r"],
    ]
)
