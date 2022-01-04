import pytest

from solutions.dcp_108.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "a, b, output",
        [
            ("abcde", "cdeab", True),
            ("abc", "acb", False),
        ],
    )
    def test_solution(self, a, b, output):
        assert solution(a, b) == output
