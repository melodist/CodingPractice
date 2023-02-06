"""
https://leetcode.com/problems/lru-cache
Using LinkedHashMap
"""
#1. My Solution (1676ms)
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.make_recently(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.size and key not in self.cache:
            del self.cache[list(self.cache.keys())[0]]

        self.cache[key] = value
        self.make_recently(key)

    def make_recently(self, key):
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#2. Other Solution (808ms)
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        tmp = self.dict.pop(key)
        self.dict[key] = tmp
        return tmp

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]
        self.dict[key] = value
