import pytest

from solutions.dcp_79.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "arr, output",
        [
            ([10, 5, 7], True),
            ([10, 7, 5], False),
            ([10], True),
            ([], True),
            ([9, 10, 5, 7], False),
        ],
    )
    def test_solution(self, arr, output):
        assert solution(arr) == output
