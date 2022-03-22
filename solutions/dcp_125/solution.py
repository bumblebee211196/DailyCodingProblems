from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def solution(root: Optional[TreeNode], k: int) -> bool:
    if not root:
        return False

    def helper(node: Optional[TreeNode]) -> bool:
        if not node:
            return False
        if k - node.val in seen:
            return True
        seen.add(node.val)
        return helper(node.left) or helper(node.right)

    seen = set()
    return helper(root)
