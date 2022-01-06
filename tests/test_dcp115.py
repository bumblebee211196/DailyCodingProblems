import pytest

from solutions.dcp_115.solution import solution, TreeNode


class TestSolution:
    @pytest.mark.parametrize(
        "s, t, output",
        [
            (TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2)), True),
            (TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2)), False),
        ],
    )
    def test_solution(self, s, t, output):
        assert solution(s, t) == output
 