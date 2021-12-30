import pytest

from solutions.dcp_83.solution import solution, TreeNode, is_equal


class TestSolution:
    @pytest.mark.parametrize(
        "root, output",
        [
            (
                TreeNode("a", TreeNode("b", TreeNode("d"), TreeNode("e")), TreeNode("c", TreeNode("f"))),
                TreeNode("a", TreeNode("c", None, TreeNode("f")), TreeNode("b", TreeNode("e"), TreeNode("d"))),
            ),
            (None, None),
            (TreeNode("1"), TreeNode("1")),
            (TreeNode("1", TreeNode("2"), TreeNode("2")), TreeNode("1", TreeNode("2"), TreeNode("2"))),
        ],
    )
    def test_solution(self, root, output):
        assert solution(root) == output
