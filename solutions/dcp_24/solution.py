class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
        self._is_locked = False
        self._locked_descendants = 0

    def is_locked(self):
        return self._is_locked

    def lock(self):
        if self._locked_descendants > 0:
            return False
        parent = self.parent
        while parent:
            if parent._is_locked:
                return False
            parent = parent.parent
        self._is_locked = True
        parent = self.parent
        while parent:
            parent._locked_descendants += 1
            parent = parent.parent
        return True

    def unlock(self):
        if self._locked_descendants > 0:
            return False
        parent = self.parent
        while parent:
            if parent._is_locked:
                return False
            parent = parent.parent
        self._is_locked = False
        parent = self.parent
        while parent:
            parent._locked_descendants -= 1
            parent = parent.parent
        return True


A = Node("A", None)
B = Node("B", A)
C = Node("C", A)
D = Node("D", B)
E = Node("E", B)
F = Node("F", C)
G = Node("G", C)


assert B.lock()
assert B.is_locked()
assert C.lock()
assert B.unlock()
assert not B.is_locked()
assert D.lock()

assert not G.lock()
assert C.unlock()
assert G.lock()

assert F.lock()
assert E.lock()

assert A._locked_descendants == 4
assert B._locked_descendants == 2
assert C._locked_descendants == 2
