import pytest

from solutions.dcp_94.solution import solution, TreeNode


class TestSolution:
    @pytest.mark.parametrize(
        "root, output",
        [
            (TreeNode(1, TreeNode(3, TreeNode(2), TreeNode(5))), 10),
            (TreeNode(1, TreeNode(3)), 4),
        ],
    )
    def test_solution(self, root, output):
        assert solution(root) == output
