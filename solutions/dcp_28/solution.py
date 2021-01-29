def solution(words, k):
    result = []
    curr_words_len = 0
    curr_words = []
    for word in words:
        if curr_words_len + len(curr_words) + len(word) > k:
            if len(curr_words) == 1:
                result.append(curr_words[0] + ' '*(k - curr_words_len))
            else:
                num_spaces = k - curr_words_len
                spaces_between, extras = divmod(num_spaces, len(curr_words) - 1)
                for i in range(extras):
                    curr_words[i] += ' '
                result.append((' '*spaces_between).join(curr_words))
            curr_words = []
            curr_words_len = 0
        curr_words.append(word)
        curr_words_len += len(word)
    num_spaces = k - curr_words_len
    if len(curr_words) > 1:
        spaces_between, extras = divmod(num_spaces, len(curr_words) - 1)
        for i in range(extras):
            curr_words[i] += ' '
        result.append((' '*spaces_between).join(curr_words))
    else:
        result.append(curr_words[0] + ' '*(k - curr_words_len))
    return result


assert solution(['the', 'quick', 'brown', 'fox', 'jumps',
                 'over', 'the', 'lazy', 'dog'], 16) == \
    ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
assert solution(['the', 'quick', 'brown', 'fox', 'jumps', 'over'], 16) == \
    ['the  quick brown', 'fox  jumps  over']
assert solution(['the', 'quick'], 16) == ['the        quick']
assert solution(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16) == \
    ['This    is    an', 'example  of text', 'justification.  ']
assert solution(['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to',
                 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else',
                 'we', 'do'], 20) == \
    ['Science  is  what we', 'understand      well', 'enough to explain to',
     'a  computer.  Art is', 'everything  else  we', 'do                  ']
