import pytest

from solutions.dcp_68.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "m, bishops, output",
        [
            (5, [(0, 0), (1, 2), (2, 2), (4, 0)], 2),
            (5, [(0, 4), (1, 2), (2, 2), (4, 0)], 3),
            (5, [(0, 4), (4, 4), (2, 2), (4, 0)], 4),
        ],
    )
    def test_solution(self, m, bishops, output):
        assert solution(m, bishops) == output
