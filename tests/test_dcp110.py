import pytest

from solutions.dcp_110.solution import solution, TreeNode


class TestSolution:
    @pytest.mark.parametrize(
        "root, output",
        [
            (TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))), [[1, 2], [1, 3, 4], [1, 3, 5]]),
        ],
    )
    def test_solution(self, root, output):
        assert solution(root) == output
