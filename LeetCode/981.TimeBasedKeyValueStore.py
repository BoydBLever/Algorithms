# https://leetcode.com/problems/time-based-key-value-store/
from typing import Dict, List, Tuple
from bisect import bisect

class TimeMap:

    def __init__(self):
        # Initialize a dictionary to store the key-value pairs along with their timestamps
        self.store: Dict[str, List[Tuple[int, str]]] = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is not in the dictionary, initialize an empty list for it
        if key not in self.store:
            self.store[key] = []
        # Append the timestamp and value as a tuple to the list of the key
        self.store[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        # If the key is not in the dictionary, return an empty string
        if key not in self.store:
            return ""
        # Get the list of timestamps and values for the key
        time_values = self.store[key]
        # Use binary search to find the index of the timestamp in the list
        idx = bisect(time_values, (timestamp, chr(127)))
        # If the index is 0, it means there is no value set for the key at the timestamp, so return an empty string
        if idx == 0:
            return ""
        # Otherwise, return the value at the index minus 1
        return time_values[idx - 1][1]

# Testing the TimeMap class
obj = TimeMap()
obj.set("foo", "bar", 1)
results_14 = [obj.get("foo", 1), obj.get("foo", 3)]
obj.set("foo", "bar2", 4)
results_14.append(obj.get("foo", 4))
results_14

#Neetcode solution
# class TimeMap:

#     def __init__(self):
#         self.store = {}
        
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.store:
#             self.store[key] = []
#         self.store[key].append([value, timestamp])
    
#     def get(self, key: str, timestamp: int) -> str:
#         res = ""
#         values = self.store.get(key, [])

#     #binary search
#     l, r = 0, len(values) - 1
#     while l <= r:
#         m = (l + r) // 2
#         if values[m][1] <= timestamp:
#             res = values[m][0]
#             l = m + 1
#         else:
#             r = m - 1

#     return res