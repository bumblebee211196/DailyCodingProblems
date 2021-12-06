from collections import defaultdict
from typing import Any, OrderedDict


class Node:
    def __init__(self, key: str, value: Any, count: int = 1) -> None:
        self.key = key
        self.value = value
        self.count = count


class LFU:
    def __init__(self, n: int) -> None:
        self.capacity = n
        self.size = 0
        self.nodes = {}
        self.freq_count = defaultdict(OrderedDict)
        self.min_count = 1
    
    def _update(self, node: Node):
        self.freq_count[self.min_count].popitem(node.key)
        if not self.freq_count[self.min_count]:
            self.min_count += 1
        node.count += 1
        self.freq_count[node.count][node.key] = node
    
    def get(self, key: str):
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._update(node)
        return node.value
    
    def set(self, key: str, value: Any):
        if key in self.nodes:
            node = self.nodes[key]
            self._update(node)
            node.value = value
        else:
            if self.size == self.capacity:
                ekey, _ = self.freq_count[self.min_count].popitem(last=False)
                self.nodes.pop(ekey)
                self.size -= 1
            node = Node(key, value)
            self.nodes[key] = node
            self.freq_count[1][key] = node
            self.min_count = 1
            self.size += 1
