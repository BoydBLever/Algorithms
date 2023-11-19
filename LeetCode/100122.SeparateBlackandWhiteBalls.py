class Solution:
    def minimumSteps(self, s: str) -> int:
        # Find the indices of the first and last black ball ('1')
        first_black = s.find('1')
        last_black = s.rfind('1')
        
        # If there are no black balls or they are already grouped together, no steps are needed
        if first_black == -1 or first_black == last_black:
            return 0
        
        # Count the number of white balls between the first and last black ball
        return s[first_black:last_black].count('0')
