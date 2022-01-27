import pytest

from solutions.dcp_118.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "nums, output",
        [
            ([-9, -2, 0, 2, 3], [0, 4, 4, 9, 81]),
            ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
            ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ],
    )
    def test_solution(self, nums, output):
        assert solution(nums) == output
