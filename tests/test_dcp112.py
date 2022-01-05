import pytest

from solutions.dcp_112.solution import solution, TreeNode


class TestSolution:
    @pytest.mark.parametrize(
        "root, p, q, output",
        [
            (
                TreeNode(
                    3,
                    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                    TreeNode(1, TreeNode(0), TreeNode(8)),
                ),
                5,
                1,
                3,
            ),
            (
                TreeNode(
                    3,
                    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                    TreeNode(1, TreeNode(0), TreeNode(8)),
                ),
                5,
                4,
                5,
            ),
            (
                TreeNode(1, TreeNode(2)),
                1,
                2,
                1,
            ),
        ],
    )
    def test_solution(self, root, p, q, output):
        assert solution(root, p, q) == output
