from typing import List, Union


class LLNode:
    def __init__(self, val: Union[str, int], next_: 'LLNode' = None) -> None:
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


def solution(head):
    if not head: return
    new_head = None
    curr = head
    while curr:
        next_ = curr.next
        curr.next = new_head
        new_head = curr
        curr = next_
    return new_head
