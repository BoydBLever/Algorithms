# https://leetcode.com/problems/daily-temperatures/
class Solution:    
    def dailyTemperatures(self, temperatures):
        # Create an empty stack to store indices of temperatures.
        stack = []
        # Initialize the answer array with zeros, since if we don't find a warmer temperature, the answer remains zero.
        res = [0] * len(temperatures)
        
        # Iterate over the list of temperatures.
        for i, temp in enumerate(temperatures):
            # Check if the stack is not empty and the current temperature is greater than the temperature at the index at the top of the stack.
            while stack and temp > temperatures[stack[-1]]:
                # Pop the index from the stack.
                last_index = stack.pop()
                # Update the result for that index with the difference between the current index and the popped index.
                res[last_index] = i - last_index
            # Push the current index onto the stack.
            stack.append(i)
        
        return res