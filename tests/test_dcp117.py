import pytest

from solutions.dcp_117.solution import solution, TreeNode


class TestSolution:
    @pytest.mark.parametrize(
        "root, output",
        [
            (
                TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
                0,
            ),
            (
                TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5)),
                3,
            ),
        ],
    )
    def test_solution(self, root, output):
        assert solution(root) == output
