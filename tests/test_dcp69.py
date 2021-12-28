import pytest

from solutions.dcp_69.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "numbers, output",
        [
            ([-10, -10, 5, 2], 500),
            ([10, -10, 5, 2], 100),
            ([10, 10, 5, 2], 500),
            ([-10, -10, 5, -2], 500),
        ],
    )
    def test_solution(self, numbers, output):
        assert solution(numbers) == output
