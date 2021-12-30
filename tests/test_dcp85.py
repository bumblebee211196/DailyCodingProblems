import pytest

from solutions.dcp_85.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "x, y, b, output",
        [
            (1, 2, 1, 1),
            (1, 2, 0, 2),
        ],
    )
    def test_solution(self, x, y, b, output):
        assert solution(x, y, b) == output
