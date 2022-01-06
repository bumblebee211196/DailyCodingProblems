import pytest

from solutions.dcp_114.solution import solution


class TestSolution:
    @pytest.mark.parametrize(
        "sentence, delimiters, output",
        [
            ("hello/world:here", ["/", ":"], "here/world:hello"),
            ("hello/world:here/", ["/", ":"], "here/world:hello/"),
            ("hello//world:here", ["/", ":"], "here//world:hello"),
        ],
    )
    def test_solution(self, sentence, delimiters, output):
        assert solution(sentence, delimiters) == output
