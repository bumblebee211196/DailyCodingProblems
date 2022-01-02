def solution(s, word_dict):
    if not s:
        return
    res = helper(s, word_dict, {})
    return res[0].split(" ")


def helper(s, word_dict, memo):
    if s in memo:
        return memo[s]
    if not s:
        return
    result = []
    for word in word_dict:
        if s.startswith(word):
            if len(s) == len(word):
                result.append(word)
            else:
                ans = helper(s[len(word) :], word_dict, memo)
                for ele in ans:
                    result.append(f"{word} {ele}")
    memo[s] = result
    return result


assert solution("theremin", ["the", "theremin"]) == ["theremin"]
assert solution("thequickbrownfox", ["quick", "brown", "the", "fox"]) == ["the", "quick", "brown", "fox"]
assert (
    solution("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "beyond"])
    == [
        "bed",
        "bath",
        "and",
        "beyond",
    ]
    or solution("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "beyond"]) == ["bedbath", "and", "beyond"]
)
