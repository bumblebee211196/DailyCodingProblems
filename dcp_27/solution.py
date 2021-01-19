def solution(s):
    stack = []
    stack_count = 0
    for char in s:
        if char in ('{', '[', '('):
            stack.append(char)
            stack_count += 1
        else:
            if stack_count > 0:
                popped = stack.pop()
                stack_count -= 1
                if popped == '(' and char == ')' or \
                   popped == '{' and char == '}' or \
                   popped == '[' and char == ']':
                    continue
            return False
    return stack_count == 0


def solution2(s):
    braces_map = {
        "{" : "}",
        "(" : ")",
        "[" : "]"
    }
    stack = []
    for char in s:
        if stack and stack[-1] in braces_map and braces_map[stack[-1]] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0



assert solution("")
assert solution("{}")
assert solution("([])")
assert solution("([])[]({})")
assert not solution("(")
assert not solution("]")
assert not solution("((()")
assert not solution("([)]")

assert solution2("")
assert solution2("{}")
assert solution2("([])")
assert solution2("([])[]({})")
assert not solution2("(")
assert not solution2("]")
assert not solution2("((()")
assert not solution2("([)]")
