def solution(s, k):
    if k == 0 or not s:
        return ''
    if k == 1:
        return s[0]
    if len(s) <= k:
        return s
    hash_map = {'keys': 0, 'values': 0}
    i = 0
    res = ''
    for j, char in enumerate(s):
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
            hash_map['keys'] += 1
        hash_map['values'] += 1
        if hash_map['keys'] == k:
            res = s[i: j + 1]
        if hash_map['keys'] > k:
            hash_map[s[i]] -= 1
            hash_map['values'] -= 1
            if hash_map[s[i]] == 0:
                hash_map.pop(s[i])
                hash_map['keys'] -= 1
            i += 1
    return res


assert solution('abcba', 2) == 'bcb'
assert solution('abccbba', 2) == 'bccbb'
assert solution('abcbbbabbcbbadd', 2) == 'bbbabb'
assert solution('abcbbbaaaaaaaaaabbcbbadd', 2) == 'bbbaaaaaaaaaabb'
assert solution('abccbba', 3) == 'abccbba'
