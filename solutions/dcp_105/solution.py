import time
import functools

from typing import Callable
from threading import Timer


defer = None


def debounce(n: float):
    def decorate(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def _func():
                return func(*args, **kwargs)

            try:
                debounce.t.cancel()
            except:
                pass
            debounce.t = Timer(n, _func)
            debounce.t.start()

        return wrapper

    return decorate
