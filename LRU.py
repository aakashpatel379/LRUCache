import collections
import pytest

class LRUCache:

    def __init__(self, size: int):
        self.size = size
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return "No key found!"

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # add recent item to the end
            self.cache.move_to_end(key, last=True)
        elif len(self.cache) == self.size:
            # pop item from left - least recently used
            self.cache.popitem(last=False)
        self.cache[key] = value

    def delete(self, key: int):
        if key in self.cache:
            d = self.cache
            del d[key]
            self.cache = d

    def reset(self):
        self.cache = collections.OrderedDict()


lru = LRUCache(3)
lru.put(1,6)
lru.put(3,8)
lru.put(4,9)

assert lru.cache == collections.OrderedDict([(1, 6), (3, 8), (4, 9)])
print("After adding 3 key-value pairs\n", lru.cache)

lru.get(3)
assert lru.cache == collections.OrderedDict([(1, 6), (4, 9), (3, 8)])
print("After reading 3\n", lru.cache)

res = lru.get(2)
assert res == 'No key found!'
print("Attempting to read non-existent key\n", res)

lru.put(6, 11)
assert lru.cache == collections.OrderedDict([(4, 9), (3, 8), (6, 11)])
print("After adding new key\n", lru.cache)

lru.delete(1)
assert lru.cache == collections.OrderedDict([(4, 9), (3, 8), (6, 11)])
print("After attempting to delete non existent key\n", lru.cache)

lru.delete(3)
assert lru.cache == collections.OrderedDict([(4, 9), (6, 11)])
print("After successful delete\n", lru.cache)

lru.reset()
assert lru.cache == collections.OrderedDict()
print("After complete reset\n", lru.cache)

