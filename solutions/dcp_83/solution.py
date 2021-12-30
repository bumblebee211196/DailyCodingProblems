from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class TreeNode:
    val: str
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def is_equal(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and root2:
        return root1.val == root2.val and is_equal(root1.left, root2.left) and is_equal(root1.right, root2.right)
    return False


def solution(root: Union[TreeNode, None]) -> Union[TreeNode, None]:
    if not root:
        return
    root.left, root.right = root.right, root.left
    solution(root.left)
    solution(root.right)
    return root
