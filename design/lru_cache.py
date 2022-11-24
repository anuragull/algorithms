"""
Aim : 
Super fast accesses. LRU caches store items in order from most-recently used to least-recently used. 
That means both can be accessed in O(1)O(1) time.

Super fast updates. Each time an item is accessed, updating the cache takes O(1)O(1) time.

Weaknesses
Space heavy. An LRU cache tracking nn items requires a linked list of length nn, and a hash map holding nn items. 
That's O(n)O(n) space, but it's still two data structures (as opposed to one).

Cache Hit :
Cache Miss : 

Time complexity:
Access : O(1)
update : O(1)

implement using ordered
"""
# implement using ordered Dict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
         # cache hit move to the top of the queue
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val
        

    def put(self, key: int, value: int) -> None:
      
        if key in self.cache: 
            del self.cache[key]
        # if more capacity remove the blast
        self.cache[key] = value
        if len( self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
