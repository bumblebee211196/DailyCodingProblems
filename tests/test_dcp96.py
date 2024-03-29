import pytest

from solutions.dcp_96.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, output",
        [
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            ([1], [[1]]),
        ],
    )
    def test_solution(self, nums, output):
        assert solution(nums) == output
