import pytest

from solutions.dcp_75.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, output",
        [
            ([6, 1, 7, 2, 8, 3, 4, 5], 5),
            ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6),
        ],
    )
    def test_solution(self, nums, output):
        assert solution(nums) == output
