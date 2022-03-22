import pytest
from solutions.dcp_126.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "arr, k, output",
        [
            ([1, 2, 3, 4, 5, 6], 1, [2, 3, 4, 5, 6, 1]),
            ([1, 2, 3, 4, 5, 6], 2, [3, 4, 5, 6, 1, 2]),
            ([1, 2, 3, 4, 5, 6], 3, [4, 5, 6, 1, 2, 3]),
            ([1, 2, 3, 4, 5, 6], 4, [5, 6, 1, 2, 3, 4]),
            ([1, 2, 3, 4, 5, 6], 5, [6, 1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5, 6]),
        ],
    )
    def test_solution(self, arr, k, output):
        solution(arr, k)
        assert arr == output
