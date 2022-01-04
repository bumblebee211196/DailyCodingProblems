from collections import deque
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def solution(root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    stack = deque([root])
    while stack:
        node = stack.popleft()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res
