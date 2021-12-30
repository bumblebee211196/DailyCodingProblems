import pytest

from solutions.dcp_77.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "intervals, output",
        [
            (
                [(1, 3), (5, 8), (4, 10), (20, 25)],
                [(1, 3), (4, 10), (20, 25)],
            ),
            (
                [(1, 3), (5, 8), (4, 6), (20, 25)],
                [(1, 3), (4, 8), (20, 25)],
            ),
            (
                [(1, 3)],
                [(1, 3)],
            ),
        ],
    )
    def test_solution(self, intervals, output):
        assert solution(intervals) == output
