from dataclasses import dataclass
from typing import Optional

INF = float("inf")


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def solution(root: Optional[TreeNode]) -> Optional[int]:
    if not root:
        return None
    stack = [root]
    res = level = 0
    min_total = INF
    while stack:
        _stack = []
        total = 0
        while stack:
            node = stack.pop()
            total += node.val
            if node.left:
                _stack.append(node.left)
            if node.right:
                _stack.append(node.right)
        if total < min_total:
            min_total = total
            res = level
        stack.extend(_stack)
        level += 1
    return res
