import pytest

from solutions.dcp_101.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "n, output",
        [
            (4, (2, 2)),
            (9, (7, 2)),
            (10, (5, 5)),
        ],
    )
    def test_solution(self, n, output):
        assert sorted(solution(n)) == sorted(output)
