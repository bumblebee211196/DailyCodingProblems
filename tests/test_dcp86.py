import pytest

from solutions.dcp_86.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "brackets, output",
        [
            ("()())()", 1),
            (")(", 2),
            ("()()()", 0),
            ("((())())()", 0),
            ("((())())()(", 1),
        ],
    )
    def test_solution(self, brackets, output):
        assert solution(brackets) == output
