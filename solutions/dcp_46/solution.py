def solution(s):
    start = end = 0
    for i in range(len(s)):
        l1 = helper(s, i, i)
        l2 = helper(s, i, i + 1)
        l = max(l1, l2)
        if l > end - start:
            start = i - ((l - 1) // 2)
            end = i + (l // 2)
    return s[start : end + 1]


def helper(s, l, r):
    n = len(s)
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1


assert solution("aabcdcb") == "bcdcb"
assert solution("bananas") == "anana"
assert solution("bumblebee") == "ebe"
assert solution("malayalam") == "malayalam"
