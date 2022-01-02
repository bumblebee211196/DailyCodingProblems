class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root):
    def _solution(root):
        if not root:
            return 0, True
        left_count, is_left_unival = _solution(root.left)
        right_count, is_right_unival = _solution(root.right)
        is_unival = is_left_unival and is_right_unival
        if root.left and root.val != root.left.val:
            is_unival = False
        if root.right and root.val != root.right.val:
            is_unival = False
        if is_unival:
            return 1 + left_count + right_count, True
        return left_count + right_count, False

    result, _ = _solution(root)
    return result


root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

assert solution(root) == 5
assert solution(root.left) == 1
assert solution(root.right) == 4
assert solution(root.right.right) == 1
assert solution(root.right.left) == 3
