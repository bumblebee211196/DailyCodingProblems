import pytest
from solutions.dcp_93.solution import TreeNode, solution


class TestSolution:
    @pytest.mark.parametrize(
        "root, output",
        [
            (TreeNode(1, TreeNode(3, TreeNode(2), TreeNode(5))), TreeNode(3, TreeNode(2), TreeNode(5))),
        ],
    )
    def test_solution(self, root, output):
        assert solution(root) == output
