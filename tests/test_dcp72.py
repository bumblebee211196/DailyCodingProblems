import pytest

from solutions.dcp_72.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "s, edges, output",
        [
            ("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)], 3),
            ("ABACA", [(0, 1), (1, 0), (0, 2), (2, 3), (3, 4)], None),
            ("ABACA", [(0, 0), (0, 1), (0, 2), (2, 3), (3, 4)], None),
        ],
    )
    def test_solution(self, s, edges, output):
        assert solution(s, edges) == output
