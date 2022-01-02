from typing import Optional
from dataclasses import dataclass


@dataclass
class LLNode:
    val: int
    time: int
    next: Optional["LLNode"] = None


class Map:
    def __init__(self) -> None:
        self.map = {}

    def set(self, key, value, time) -> None:
        node = LLNode(value, time)
        if key not in self.map:
            self.map[key] = node
            return
        prev = curr = self.map[key]
        if time < curr.time:
            node.next = curr
            self.map[key] = node
            return
        while curr:
            if curr.time == time:
                curr.val = value
                return
            if curr.time > time:
                break
            prev = curr
            curr = curr.next
        prev.next = node
        node.next = curr

    def get(self, key, time) -> Optional[int]:
        if key not in self.map:
            return None
        curr = self.map[key]
        res = None
        while curr:
            if curr.time == time:
                return curr.val
            if curr.time < time:
                res = curr.val
            curr = curr.next
        return res
