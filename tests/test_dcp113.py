import pytest

from solutions.dcp_113.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "s, output",
        [
            ("hello world here", "here world hello"),
        ],
    )
    def test_solution(self, s, output):
        assert solution(s) == output
