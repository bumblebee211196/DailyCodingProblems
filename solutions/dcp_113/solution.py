import re


def solution(s: str) -> str:
    # Since python doesn't have mutable string, we will use list to solve it in in-place.
    s = re.sub(r"[ ]+", " ", s)
    s = list(s.strip())
    start = end = 0
    for i in range(len(s)):
        if s[i] == " ":
            subs = s[start : end + 1]
            s[start : end + 1] = subs[::-1]
            start = i + 1
        end = i
    subs = s[start : end + 1]
    s[start : end + 1] = subs[::-1]
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)
