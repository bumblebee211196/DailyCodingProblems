from typing import Optional, Union
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def solution(root: TreeNode, p, q) -> int:
    def dfs(node: Optional[TreeNode]) -> Union[int, bool]:
        if not node:
            return False
        if node.val in (p, q):
            return node.val
        left = dfs(node.left)
        right = dfs(node.right)
        if left and right:
            return node.val
        return left or right

    return dfs(root)
