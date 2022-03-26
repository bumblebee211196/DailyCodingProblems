from typing import Any


class Singleton(type):

    instances = {}
    calls = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        # Increase call count
        cls.calls[cls] = cls.calls.get(cls, 0) + 1
        calls = cls.calls[cls]
        instances = cls.instances.get(cls, [])
        # Handle even cases
        if calls % 2 == 0:
            if len(instances) == 2:
                return instances[1]
            obj = super(Singleton, cls).__call__(*args, **kwds)
            cls.instances[cls].append(obj)
            return obj
        # Handle odd cases
        if len(instances) > 0:
            return instances[0]
        obj = super(Singleton, cls).__call__(*args, **kwds)
        cls.instances[cls] = [obj]
        return obj
