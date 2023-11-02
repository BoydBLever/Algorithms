class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            self.cache[key] = value
        else:
            if len(self.order) == self.capacity:
                self.cache.pop(self.order[0])
                self.order.pop(0)
            self.order.append(key)
            self.cache[key] = value
        return None
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)