from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


def get_preorder(root: Optional[TreeNode]) -> str:
    if root:
        return f"#{root.val} {get_preorder(root.left)} {get_preorder(root.right)}"
    return ""


def solution(s: TreeNode, t: TreeNode) -> bool:
    return get_preorder(t) in get_preorder(s)
