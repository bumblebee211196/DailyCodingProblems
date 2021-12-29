import pytest

from solutions.dcp_74.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "n, x, output",
        [
            (6, 12, 4),
            (6, 16, 1),
            (16, 16, 2),
        ],
    )
    def test_solution(self, n, x, output):
        assert solution(n, x) == output
