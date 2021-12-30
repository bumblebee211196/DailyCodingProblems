MAPPINGS = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def solution(digit: str):
    def _solution(index: int, curr: str):
        if index >= len(digit):
            return [curr]
        res = []
        for char in MAPPINGS[digit[index]]:
            res.extend(_solution(index + 1, f"{curr}{char}"))
        return res

    if not digit:
        return []
    return _solution(0, "")
