import sys

from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def solution(root: Optional[TreeNode]) -> int:
    def helper(node: Optional[TreeNode]) -> int:
        nonlocal res
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        temp = left + node.val + right
        res = max(res, temp)
        return max(left + node.val, node.val + right)

    res = -sys.maxsize
    helper(root)
    return res
