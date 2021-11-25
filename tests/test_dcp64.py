import pytest

from solutions.dcp_64.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "n, output",
        [
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 1728),
        ],
    )
    def test_solution(self, n, output):
        assert solution(n) == output
