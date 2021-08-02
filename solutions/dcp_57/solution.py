def solution(s, k):
    if not s:
        return []
    words = s.split(" ")
    result = []
    curr_word = ""
    for word in words:
        if not curr_word:
            curr_word = word
        elif len(word) + 1 <= k - len(curr_word):
            curr_word = f"{curr_word} {word}"
        else:
            result.append(curr_word)
            curr_word = word
    if curr_word:
        result.append(curr_word)
    return result


assert solution("the quick brown fox jumps over the lazy dog", 10) == [
    "the quick",
    "brown fox",
    "jumps over",
    "the lazy",
    "dog",
]
assert solution("What must be acknowledgment shall be", 16) == ["What must be", "acknowledgment", "shall be"]
assert solution(
    "Science is what we understand well enough to explain to a computer. Art is everything else we do", 20
) == ["Science is what we", "understand well", "enough to explain to", "a computer. Art is", "everything else we", "do"]
assert solution("", 10) == []
