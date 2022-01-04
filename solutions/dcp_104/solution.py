from typing import Optional
from dataclasses import dataclass


@dataclass
class LLNode:
    val: int
    next: Optional["LLNode"] = None


def solution(head: LLNode) -> bool:
    if not head:
        return True
    nodes = []
    curr = head
    while curr:
        nodes.append(curr.val)
        curr = curr.next
    return nodes == nodes[::-1]
