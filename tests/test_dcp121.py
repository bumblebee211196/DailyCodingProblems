import pytest
from solutions.dcp_121.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "s, k, output",
        [
            ("waterrfetawx", 2, True),
            ("nitabin", 1, False),
        ],
    )
    def test_solution(self, s, k, output):
        assert solution(s, k) == output
