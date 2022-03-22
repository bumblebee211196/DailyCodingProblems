import pytest
from solutions.dcp_125.solution import TreeNode, solution


class TestSolution:
    @pytest.mark.parametrize(
        "root, k, output",
        [
            (TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(11), TreeNode(15))), 20, True),
            (TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(11), TreeNode(15))), 15, True),
            (TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(11), TreeNode(15))), 0, False),
        ],
    )
    def test_solution(self, root, k, output):
        assert solution(root, k) == output
