import pytest

from solutions.dcp_1.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "arr, k, output",
        [
            ([10, 15, 3, 7, 19, 12, 1, 8], 27, True),
            ([10, 15, 3, 7, 19, 12, 1, 8], 50, False),
            ([], 10, False),
            ([1], 10, False),
        ],
    )
    def test_solution(self, arr, k, output):
        assert solution(arr, k) == output
