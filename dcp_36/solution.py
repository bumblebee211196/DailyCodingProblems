class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{}'.format(self.val)

    __repr__ = __str__


def solution(node):
    res = []
    def _solution(node, counter):
        if not node or counter[0] >= 2:
            return
        _solution(node.right, counter)
        counter[0] += 1
        if counter[0] == 2:
            res.append(node.val)
            return
        _solution(node.left, counter)
    _solution(node, [0])
    if res:
        return res[0]
    return None


node_a = Node(5)
node_b = Node(3)
node_c = Node(8)
node_d = Node(2)
node_e = Node(4)
node_f = Node(7)
node_g = Node(9)
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

assert solution(node_a) == 8

node_a = Node(5)
node_b = Node(3)
node_d = Node(2)
node_e = Node(4)
node_a.left = node_b
node_b.left = node_d
node_b.right = node_e

assert solution(node_a) == 4

node_a = Node(5)

assert not solution(node_a)

node_a = Node(5)
node_b = Node(3)
node_d = Node(2)
node_a.left = node_b
node_b.left = node_d

assert solution(node_a) == 3
