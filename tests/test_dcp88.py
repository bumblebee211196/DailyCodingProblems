import pytest

from solutions.dcp_88.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "x, y, output",
        [
            (100, 1, 100),
            (100, 2, 50),
            (100, 3, 33),
            (100, 4, 25),
            (100, 5, 20),
            (100, 6, 16),
            (100, 7, 14),
            (100, 8, 12),
            (100, 9, 11),
            (100, 10, 10),
        ],
    )
    def test_solution(self, x, y, output):
        assert solution(x, y) == output
