import pytest

from solutions.dcp_80.solution import solution, TreeNode


class TestSolution:
    @pytest.mark.parametrize(
        "root, output",
        [
            (TreeNode("a", TreeNode("b", TreeNode("d")), TreeNode("c")), "d"),
        ],
    )
    def test_solution(self, root, output):
        assert solution(root) == output
