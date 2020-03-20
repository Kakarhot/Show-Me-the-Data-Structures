from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables        
        self.cache = {}
        self.capacity = capacity
        self.queue = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.cache:
            if len(self.cache.keys()) == self.capacity:
                removed_key = self.queue.popleft()
                self.cache.pop(removed_key)
                
            self.cache[key] = value
            self.queue.append(key)


our_cache = LRU_Cache(2)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 2)
print(our_cache.cache)
print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns 2
print(our_cache.get(None))    # return -1