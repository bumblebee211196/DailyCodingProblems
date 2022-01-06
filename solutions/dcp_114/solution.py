from typing import List


def solution(sentence: str, delimiters: List[int]) -> str:
    words = []
    res = []
    word = ""
    for c in sentence:
        if c in delimiters:
            if word:
                words.append(word)
                res.append("")
            res.append(c)
            word = ""
        else:
            word += c
    if word:
        words.append(word)
        res.append("")
    for i, word in enumerate(res):
        if word == "":
            res[i] = words.pop()
    return "".join(res)
