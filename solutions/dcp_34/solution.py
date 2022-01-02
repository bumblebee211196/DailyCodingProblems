cache = {}


def is_pallindrome(s):
    return s == s[::-1]


def solution(s):
    if s in cache:
        return cache[s]
    if is_pallindrome(s):
        cache[s] = s
        return s
    if s[0] == s[-1]:
        res = s[0] + solution(s[1:-1]) + s[-1]
        cache[s] = res
        return res
    first = s[0] + solution(s[1:]) + s[0]
    second = s[-1] + solution(s[:-1]) + s[-1]
    if len(first) < len(second):
        res = first
    elif len(second) < len(first):
        res = second
    else:
        res = min(first, second)
    cache[s] = res
    return res


assert solution("racecar") == "racecar"
assert solution("google") == "elgoogle"
assert solution("egoogle") == "elgoogle"
assert solution("elgoog") == "elgoogle"
assert solution("race") == "ecarace"
