class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(preorder, inorder):
    if not preorder:
        return
    root = Tree(preorder[0])
    root_idx = inorder.index(root.val)
    root.left = solution(preorder[1 : 1 + root_idx], inorder[:root_idx])
    root.right = solution(preorder[1 + root_idx :], inorder[1 + root_idx :])
    return root


tree = solution(preorder=["a", "b", "d", "e", "c", "f", "g"], inorder=["d", "b", "e", "a", "f", "c", "g"])
assert tree.val == "a"
assert tree.left.val == "b"
assert tree.left.left.val == "d"
assert tree.left.right.val == "e"
assert tree.right.val == "c"
assert tree.right.left.val == "f"
assert tree.right.right.val == "g"

tree = solution(preorder=["a", "b", "d", "e", "c", "g"], inorder=["d", "b", "e", "a", "c", "g"])
assert tree.val == "a"
assert tree.left.val == "b"
assert tree.left.left.val == "d"
assert tree.left.right.val == "e"
assert tree.right.val == "c"
assert tree.right.right.val == "g"
