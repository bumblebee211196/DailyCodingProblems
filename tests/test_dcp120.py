from solutions.dcp_120.solution import Singleton


class DummyClass(metaclass=Singleton):
    pass


class TestSolution:
    def test_solution(self):
        obj1 = DummyClass()
        obj2 = DummyClass()

        assert obj1 is DummyClass()
        assert obj2 is DummyClass()
        assert obj1 is not obj2
