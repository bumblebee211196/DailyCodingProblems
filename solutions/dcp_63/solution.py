def solution(matrix, word):
    if not matrix:
        return False
    for row in matrix:
        if word in "".join(row):
            return True
    for col in zip(*matrix):
        if word in "".join(col):
            return True
    return False


MATRIX = [["F", "A", "C", "I"], ["O", "B", "Q", "P"], ["A", "N", "O", "B"], ["M", "A", "S", "S"]]

assert solution(MATRIX, "FOAM") == True
assert solution(MATRIX, "MASS") == True
assert solution(MATRIX, "QOS") == True
assert solution(MATRIX, "IPO") == False
