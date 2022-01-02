import pytest

from solutions.dcp_99.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, output",
        [
            ([100, 4, 200, 1, 3, 2], 4),
            ([100, 4, 200, 1, 3, 2, 101, 105, 103, 102, 104], 6),
        ],
    )
    def test_solution(self, nums, output):
        assert solution(nums) == output
