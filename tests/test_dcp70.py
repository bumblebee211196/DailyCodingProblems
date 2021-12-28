import pytest

from solutions.dcp_70.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "n, output",
        [
            (1, 19),
            (2, 28),
            (5, 55),
            (10, 109),
            (100, 1423),
            (500, 18010),
            (1000, 100036),
            (10000, 10800100),
        ],
    )
    def test_solution(self, n, output):
        assert solution(n) == output
