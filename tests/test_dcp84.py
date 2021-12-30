import pytest

from solutions.dcp_84.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "grid, output",
        [
            ([
                [1,0,0,0,0],
                [0,0,1,1,0],
                [0,1,1,0,0],
                [0,0,0,0,0],
                [1,1,0,0,1],
                [1,1,0,0,1]
            ], 4
            ),
            ([
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ], 0),
            ([
                [0,0,0],
                [0,1,0],
                [0,0,0]
            ], 1),
        ],
    )
    def test_solution(self, grid, output):
        assert solution(grid) == output
