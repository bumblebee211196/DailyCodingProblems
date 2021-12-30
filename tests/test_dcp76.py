import pytest

from solutions.dcp_76.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "letters, output",
        [
            (
                [
                    ["c", "b", "a"],
                    ["d", "a", "f"],
                    ["g", "h", "i"],
                ],
                1,
            ),
            ([["a", "b", "c", "d", "e", "f"]], 0),
            (
                [
                    ["z", "y", "x"],
                    ["w", "v", "u"],
                    ["t", "s", "r"],
                ],
                3,
            ),
        ],
    )
    def test_solution(self, letters, output):
        assert solution(letters) == output
