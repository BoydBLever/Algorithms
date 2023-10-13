# https://leetcode.com/problems/car-fleet/
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples (position, time required to reach the target) for each car
        # Time required to reach the target = (target - position) / speed
        cars = sorted([(pos, (target - pos) / spd) for pos, spd in zip(position, speed)], reverse=True)
        
        # Initialize result as 0
        res = 0
        
        # Initialize the previous car's time to 0
        prev_time = 0
        
        # Iterate over each car's time required to reach the target
        for _, time in cars:
            # If current car's time is greater than the previous car's time, then it forms a new fleet
            if time > prev_time:
                res += 1
                prev_time = time  # Update the previous car's time
        
        return res

# Testing the function on given examples
test_cases_2 = [
    (12, [10,8,0,5,3], [2,4,1,1,3], 3),
    (10, [3], [3], 1),
    (100, [0,2,4], [4,2,1], 1)
]

results_2 = [(test[:-1], Solution().carFleet(*test[:-1]) == test[-1]) for test in test_cases_2]
results_2
