def solution(s, pattern):
    memo = {}
    def helper(i, j):
        if (i, j) in memo:
            return memo[i, j]
        result = False
        if j == len(pattern):
            return i == len(s)
        # Check if the first element matches
        first_match = i < len(s) and pattern[j] in (s[i], '.')
        # If the next pattern is a wild card
        # Either the string must have the character once or not at all
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            # First one is the character occured once
            # Second one is the character has no occurence at all
            result = first_match and helper(i + 1, j) or helper(i, j + 2)
        else:
            # If not a wild character, proceed as normal
            result = first_match and helper(i + 1, j + 1)
        memo[i, j] = result
        return result
    return helper(0, 0)


assert solution("ray", "ra.")
assert not solution("ra.", "raymond")
assert solution("chat", ".*at")
assert not solution("chats", ".*at")
assert solution("st", "s*t")
assert not solution("", "cat")
assert solution("", "")
assert solution("sathish", "s.*this.*")
