from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        
        for op in operations:
            # if x = integer, add x to array
            if op.lstrip('-').isdigit():
                score.append(int(op))
            # if +, add a new score that is the sum of previous two
            elif op == '+':
                score.append(score[-1] + score[-2])
            # if D, add a new score that is double the previous score
            elif op == 'D':
                score.append(score[-1] * 2)
            # if C, invalidate the previous score, removing it from the record
            elif op == 'C':
                score.pop()
        # sum all the scores on the record
        return sum(score)

    
# Test processing function
test = Solution() # instantiate class
print(test.calPoints(["5","2","C","D","+"])) # 30