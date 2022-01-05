from typing import List, Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def solution(root: TreeNode) -> List[List[int]]:
    def helper(node: TreeNode, curr: List[int]) -> None:
        if not node.left and not node.right:
            curr.append(node.val)
            res.append(curr.copy())
            return
        if node.left:
            helper(node.left, curr + [node.val])
        if node.right:
            helper(node.right, curr + [node.val])

    if not root:
        return []
    res = []
    helper(root, [])
    return res
