"""
https://leetcode.com/problems/lfu-cache
Using dict instead of LinkedHashSet
"""
#1. My Solution (1095ms)
class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_value = dict()
        self.key_to_freq = dict()
        self.freq_to_keys = defaultdict(dict)
        self.cap = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1
            
        self.increase_freq(key)
        return self.key_to_value[key]
        
    def put(self, key: int, value: int) -> None:
        if self.cap <= 0: return

        if key in self.key_to_value:
            self.key_to_value[key] = value
            self.increase_freq(key)
            return

        if self.cap <= len(self.key_to_value):
            self.remove_min_freq_key()

        self.key_to_value[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = key
        self.min_freq = 1

    def remove_min_freq_key(self):
        key_list = self.freq_to_keys[self.min_freq]
        deleted_key = next(iter(key_list))

        del key_list[deleted_key]

        if not key_list:
            del self.freq_to_keys[self.min_freq]

        del self.key_to_value[deleted_key]
        del self.key_to_freq[deleted_key] 

    def increase_freq(self, key):
        freq = self.key_to_freq[key]
        self.key_to_freq[key] = freq + 1

        del self.freq_to_keys[freq][key]
        self.freq_to_keys[freq + 1][key] = key

        if len(self.freq_to_keys[freq]) == 0:
            del self.freq_to_keys[freq]

            if freq == self.min_freq:
                self.min_freq += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
