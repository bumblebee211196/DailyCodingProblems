class LogOrderIds:
    def __init__(self, n):
        self.size = n
        self.index = 0
        self.log = [-1] * n

    def record(self, order_id):
        self.index = self.index % self.size
        self.log[self.index] = order_id
        self.index += 1

    def get_last(self, i):
        return self.log[(self.index - i + self.size) % self.size]


log = LogOrderIds(5)
log.record(1)
log.record(2)
log.record(3)
log.record(4)
log.record(5)
assert log.get_last(5) == 1
assert log.get_last(4) == 2
assert log.get_last(3) == 3
log.record(6)
log.record(7)
log.record(8)
assert log.get_last(5) == 4
assert log.get_last(4) == 5
assert log.get_last(3) == 6
assert log.get_last(2) == 7
assert log.get_last(1) == 8
