import time

from dataclasses import dataclass

from solutions.dcp_105.solution import debounce


@dataclass
class SomeClass:
    n = 0

    @debounce(1)
    def inc(self) -> None:
        self.n += 1


class TestSolution:
    def test_solution1(self):
        obj = SomeClass()
        for _ in range(5):
            obj.inc()
        time.sleep(1.1)
        assert obj.n == 1

    def test_solution2(self):
        obj = SomeClass()
        for _ in range(5):
            obj.inc()
            time.sleep(1.1)
        time.sleep(1.1)
        assert obj.n == 5

    def test_solution3(self):
        obj = SomeClass()
        for _ in range(5):
            obj.inc()
        assert obj.n == 0
