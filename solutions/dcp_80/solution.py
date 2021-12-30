from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: str
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


def solution(root: TreeNode):
    if not root:
        return None
    stack = [root]
    res = None
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        res = node.val
    return res
