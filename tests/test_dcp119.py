import pytest
from solutions.dcp_119.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "intervals, output",
        [([[0, 3], [2, 6], [3, 4], [6, 9]], {9, 3})],
    )
    def test_solution(self, intervals, output):
        assert solution(intervals) == output
