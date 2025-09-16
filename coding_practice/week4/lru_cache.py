"""
LRU Cache - LeetCode #146
Design a Least Recently Used (LRU) cache with O(1) get and put.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # remove LRU

# Quick test
lru = LRUCache(2)
lru.put(1,1); lru.put(2,2)
print(lru.get(1))  # 1
lru.put(3,3)       # evicts key 2
print(lru.get(2))  # -1
