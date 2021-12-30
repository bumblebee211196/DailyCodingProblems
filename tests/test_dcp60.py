import pytest

from solutions.dcp_60.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "arr, output",
        [
            ([15, 5, 20, 10, 35, 15, 10], True),
            ([15, 5, 20, 10, 35], False),
        ],
    )
    def test_solution(self, arr, output):
        assert solution(arr) == output
