import pytest

from solutions.dcp_111.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "w, s, output",
        [
            ("ab", "abxaba", [0, 3, 4]),
        ],
    )
    def test_solution(self, w, s, output):
        assert solution(w, s) == output
