import pytest

from solutions.dcp_81.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "digit, output",
        [("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]), ("2", ["a", "b", "c"]), ("", [])],
    )
    def test_solution(self, digit, output):
        assert solution(digit) == output
