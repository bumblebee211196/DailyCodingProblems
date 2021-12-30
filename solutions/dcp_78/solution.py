import heapq
from typing import List, Union


class LLNode:
    def __init__(self, val, next_=None) -> None:
        self.val = val
        self.next = next_


def ll_to_list(head: LLNode) -> List[Union[str, int]]:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


def list_to_ll(vals: List[Union[str, int]]) -> LLNode:
    head = curr = None
    for val in vals:
        node = LLNode(val)
        if not head:
            head = curr = node
            continue
        curr.next = node
        curr = curr.next
    return head


def solution(llnodes: List[LLNode]) -> Union[LLNode, None]:
    n = len(llnodes)
    if n == 0:
        return None
    if n == 1:
        return llnodes[0]
    vals = []
    for head in llnodes:
        while head:
            heapq.heappush(vals, head.val)
            head = head.next
    head = curr = None
    while vals:
        node = LLNode(heapq.heappop(vals))
        if not head:
            curr = head = node
            continue
        curr.next = node
        curr = curr.next
    return head
