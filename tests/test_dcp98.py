import pytest

from solutions.dcp_98.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "word, output",
        [
            ("ABCCED", True),
            ("SEE", True),
            ("ABCB", False),
        ],
    )
    def test_solution(self, word, output):
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        assert solution(board, word) == output
