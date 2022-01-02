def solution(brackets: str) -> int:
    left = right = 0
    for b in brackets:
        if b == "(":
            left += 1
        elif b == ")":
            if left > 0:
                left -= 1
            else:
                right += 1
    return left + right
