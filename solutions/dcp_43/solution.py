class Stack:
    def __init__(self):
        self._top = -1
        self._stack = []
        self._max_till = []

    def push(self, val):
        self._stack.append(val)
        if self._top < 0:
            self._max_till.append(val)
        else:
            self._max_till.append(max(self._max_till[self._top], val))
        self._top += 1

    def pop(self):
        if self._top < 0:
            return
        val = self._stack[self._top]
        self._top -= 1
        return val

    def max(self):
        if self._top < 0:
            return
        return self._max_till[self._top]


stack = Stack()
stack.push(1)
stack.push(3)
stack.push(2)
stack.push(5)
assert stack.max() == 5
stack.pop()
assert stack.max() == 3
stack.pop()
assert stack.max() == 3
stack.pop()
assert stack.max() == 1
stack.pop()
assert not stack.max()

stack = Stack()
stack.push(10)
stack.push(3)
stack.push(2)
stack.push(5)
assert stack.max() == 10
stack.pop()
assert stack.max() == 10
stack.pop()
assert stack.max() == 10
stack.pop()
assert stack.max() == 10
stack.pop()
assert not stack.max()
