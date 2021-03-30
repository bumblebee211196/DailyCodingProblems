from collections import OrderedDict


class LRU:
    def __init__(self, n):
        self._capacity = n
        self._size = 0
        self._cache = OrderedDict()

    def set(self, key, value):
        if key in self._cache:
            self._cache.pop(key)
            self._cache[key] = value
        else:
            if self._size < self._capacity:
                self._cache[key] = value
                self._size += 1
            else:
                self._cache.pop(list(self._cache.keys())[0])
                self._cache[key] = value

    def get(self, key):
        if key in self._cache:
            value = self._cache[key]
            self._cache.pop(key)
            self._cache[key] = value
            return value
        return None


lru = LRU(3)

assert not lru.get("a")
lru.set("a", 1)
assert lru.get("a") == 1
lru.set("b", 2)
lru.set("c", 3)
lru.set("d", 4)
lru.set("e", 5)
lru.set("a", 1)
assert lru.get("a") == 1
assert not lru.get("b")
assert lru.get("e") == 5
assert not lru.get("c")
