import ctypes


def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value


class Node:

    def __init__(self, val):
        self.val = val
        self.both = 0


class XORLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.__nodes = []

    def add(self, element):
        node = Node(element)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.both = id(self.tail)
            self.tail.both = id(node) ^ self.tail.both
            self.tail = node

    def get(self, index):
        head = self.head
        prev = 0
        for i in range(index):
            next = head.both ^ prev
            if next:
                prev = id(head)
                head = _get_obj(next)
        return head.val


xor_ll = XORLinkedList()
xor_ll.add('1')
xor_ll.add('2')
xor_ll.add('3')

assert xor_ll.get(0) == '1'
assert xor_ll.get(1) == '2'
assert xor_ll.get(2) == '3'
