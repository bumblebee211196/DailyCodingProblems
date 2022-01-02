import pytest

from solutions.dcp_100.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "points, output",
        [
            ([(0, 0), (1, 1), (1, 2)], 2),
            ([(0, 0), (1, 1), (1, 2), (2, 2), (3, 3)], 4),
        ],
    )
    def test_solution(self, points, output):
        assert solution(points) == output
