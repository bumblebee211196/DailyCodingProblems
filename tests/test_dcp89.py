import pytest

from solutions.dcp_89.solution import solution, TreeNode


class TestSolution:
    @pytest.mark.parametrize(
        "root, output",
        [
            (TreeNode(3, TreeNode(2), TreeNode(9)), True),
            (TreeNode(3, TreeNode(9), TreeNode(2)), False),
            (None, True),
            (TreeNode(3, TreeNode(2), TreeNode(9, TreeNode(7, TreeNode(4), TreeNode(8)), TreeNode(12))), True),
            (TreeNode(3, TreeNode(1), TreeNode(5, TreeNode(4, None, TreeNode(7)), TreeNode(6))), False),
        ],
    )
    def test_solution(self, root, output):
        assert solution(root) == output
