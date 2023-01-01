# Design LRU Cache in python
# Using Simple Dictionary

#from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            return self.cache[key]
            # value of the key is - how many times it is accessed .
            self.cache[key] = self.cache[key]+1

    def push(self,key,data):
        if key in self.cache:
            return -1
        else:
            if len(self.cache) == self.capacity:
                print('cache eviction in progress')
                try:
                    self.cache = {a:b for a,b in sorted(self.cache.items(),key=lambda item:item[1])}
                    self.cache.popitem()
                except:
                    print('cache eviction in progress and it was failed')
                    return -1
            self.cache[key] = data