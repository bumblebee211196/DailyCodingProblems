import pytest

from solutions.dcp_104.solution import solution, LLNode


class TestSolution:
    @pytest.mark.parametrize(
        "head, output",
        [
            (LLNode(1, LLNode(4, LLNode(3, LLNode(4, LLNode(1))))), True),
            (LLNode(1, LLNode(4, LLNode(4, LLNode(1)))), True),
            (LLNode(1, LLNode(4)), False),
        ],
    )
    def test_solution(self, head, output):
        assert solution(head) == output
