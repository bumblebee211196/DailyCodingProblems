import pytest

from solutions.dcp_2.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "arr, output",
        [
            ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
            ([1, 2, 0, 3, 5], [0, 0, 30, 0, 0]),
            ([3, 2, 1], [2, 3, 6]),
            ([], []),
        ],
    )
    def test_solution(self, arr, output):
        assert solution(arr) == output
