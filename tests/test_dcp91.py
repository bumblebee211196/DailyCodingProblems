import pytest

from solutions.dcp_92.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "courses, output",
        [
            ({"CSC300": ["CSC100", "CSC200"], "CSC200": ["CSC100"], "CSC100": []}, ["CSC100", "CSC200", "CSC300"]),
            ({"CSC300": ["CSC200"], "CSC200": ["CSC100"], "CSC100": ["CSC300"]}, None),
        ],
    )
    def test_solution(self, courses, output):
        assert solution(courses) == output
