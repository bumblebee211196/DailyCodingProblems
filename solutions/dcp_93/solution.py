import sys

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def solution(root: TreeNode) -> Optional[TreeNode]:
    def helper(node: Optional[TreeNode]) -> Tuple[bool, int, int, int]:
        nonlocal res, max_size
        if not node:
            return True, sys.maxsize, -sys.maxsize, 0
        is_left_bst, lmin, lmax, lsize = helper(node.left)
        is_right_bst, rmin, rmax, rsize = helper(node.right)
        if is_left_bst and is_right_bst and lmax < node.val < rmin:
            size = 1 + lsize + rsize
            if size > max_size:
                max_size = size
                res = node
            return True, min(lmin, node.val), max(rmax, node.val), size
        return False, sys.maxsize, -sys.maxsize, 0

    max_size, res = 0, None
    helper(root)
    return res
