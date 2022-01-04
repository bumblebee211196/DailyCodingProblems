import pytest

from solutions.dcp_106.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "arr, output",
        [
            ([2, 0, 1, 0], True),
            ([1, 1, 0, 1], False),
        ],
    )
    def test_solution(self, arr, output):
        assert solution(arr) == output
