import pytest

from solutions.dcp_78.solution import solution, ll_to_list, list_to_ll


class TestSolution:
    @pytest.mark.parametrize(
        "vals, output",
        [
            (
                [[1, 3, 5, 7, 9], [2, 4, 6, 8]],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
            ),
            ([], []),
            ([[1]], [1]),
        ],
    )
    def test_solution(self, vals, output):
        llnodes = []
        for vals_ in vals:
            llnodes.append(list_to_ll(vals_))
        assert ll_to_list(solution(llnodes)) == output
