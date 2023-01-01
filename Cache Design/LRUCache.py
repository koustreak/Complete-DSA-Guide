# Design LRU Cache in python
# Using Simple Dictionary

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            return self.cache[key]
            self.cache.move_to_end(key)

    def push(self,key,data):
        if key in self.cache:
            return -1
        else:
            if len(self.cache) == self.capacity:
                print('cache eviction in progress')
                try:
                    self.cache.popitem(last=False)
                except:
                    print('cache eviction in progress and it was failed')
                    return -1
            self.cache[key] = data