import pytest
from solutions.dcp_122.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "matrix, output",
        [
            ([[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]], 12),
        ],
    )
    def test_solution(self, matrix, output):
        assert solution(matrix) == output
