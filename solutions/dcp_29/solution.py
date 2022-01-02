def encode_string(s):
    prev_char = None
    char_count = 0
    result = ""
    for char in s:
        if prev_char:
            if char == prev_char:
                char_count += 1
            else:
                result = "{}{}{}".format(result, char_count, prev_char)
                prev_char = char
                char_count = 1
        else:
            prev_char = char
            char_count = 1
    if char_count > 0:
        result = "{}{}{}".format(result, char_count, prev_char)
    return result


def decode_string(s):
    result = ""
    for i in range(0, len(s), 2):
        num, char = int(s[i]), s[i + 1]
        result = "{}{}".format(result, ("{}".format(char)) * num)
    return result


assert encode_string("") == ""
assert encode_string("AAA") == "3A"
assert encode_string("AAAABBBCCDAA") == "4A3B2C1D2A"

assert decode_string("") == ""
assert decode_string("3A") == "AAA"
assert decode_string("4A3B2C1D2A") == "AAAABBBCCDAA"
