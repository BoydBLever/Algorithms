# Twitch interview question
# https://leetcode.com/problems/lru-cache/description/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # Left=LRU, right=most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from List
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the List and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        




#Solution 2:
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.order = []
        

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.order.remove(key)
#             self.order.append(key)
#             return self.cache[key]
#         else:
#             return -1
        
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.order.remove(key)
#             self.order.append(key)
#             self.cache[key] = value
#         else:
#             if len(self.order) == self.capacity:
#                 self.cache.pop(self.order[0])
#                 self.order.pop(0)
#             self.order.append(key)
#             self.cache[key] = value
#         return None
    
    #time complexity: O(n)
    #space complexity: O(n)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)