import sys


class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode) -> bool:
    def helper(node: TreeNode, low: int, high: int):
        if not node:
            return True
        if low < node.val < high:
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        return False

    return helper(root, -sys.maxsize, sys.maxsize)
