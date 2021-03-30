class Queue:
    def __init__(self):
        self._stack = []

    def enqueue(self, val):
        self._stack.append(val)

    def dequeue(self):
        if self._stack:
            temp = []
            while self._stack:
                temp.append(self._stack.pop())
            val = temp.pop()
            while temp:
                self._stack.append(temp.pop())
            return val
        return None


q = Queue()
q.enqueue(1)
assert q._stack == [1]
q.enqueue(2)
assert q._stack == [1, 2]
q.enqueue(3)
assert q._stack == [1, 2, 3]
val = q.dequeue()
assert val == 1
assert q._stack == [2, 3]
val = q.dequeue()
assert val == 2
assert q._stack == [3]
