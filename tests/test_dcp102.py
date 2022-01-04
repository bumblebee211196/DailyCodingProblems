import pytest

from solutions.dcp_102.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, k, output",
        [
            ([1, 2, 3, 4, 5], 1, [1]),
            ([1, 2, 3, 4, 5], 2, [2]),
            ([1, 2, 3, 4, 5], 3, [1, 2]),
            ([1, 2, 3, 4, 5], 4, [4]),
            ([1, 2, 3, 4, 5], 5, [2, 3]),
            ([1, 2, 3, 4, 5], 6, [1, 2, 3]),
            ([1, 2, 3, 4, 5], 7, [3, 4]),
            ([1, 2, 3, 4, 5], 9, [2, 3, 4]),
            ([1, 2, 3, 4, 5], 10, [1, 2, 3, 4]),
        ],
    )
    def test_solution(self, nums, k, output):
        assert solution(nums, k) == output
