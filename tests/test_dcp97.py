import pytest

from solutions.dcp_97.solution import Map


class TestSolution:
    def setup_method(self, _):
        self.d = Map()

    def test_solution_case1(self):
        self.d.set(1, 1, 0)
        self.d.set(1, 2, 2)
        assert self.d.get(1, 1) == 1
        assert self.d.get(1, 3) == 2

    def test_solution_case2(self):
        self.d.set(1, 1, 5)
        assert self.d.get(1, 0) is None
        assert self.d.get(1, 10) == 1

    def test_solution_case3(self):
        self.d.set(1, 1, 0)
        self.d.set(1, 2, 0)
        assert self.d.get(1, 0) == 2

    def teardown_method(self, _):
        del self.d
