import pytest

from solutions.dcp_73.solution import solution, list_to_ll, ll_to_list


class TestSolution:
    @pytest.mark.parametrize(
        "vals, output",
        [
            ([1,2,3,4,5], [5,4,3,2,1]),
            ([], []),
            ([1], [1]),
        ],
    )
    def test_solution(self, vals, output):
        assert ll_to_list(solution(list_to_ll(vals))) == output
