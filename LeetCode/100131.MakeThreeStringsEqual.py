class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # Check if the lengths of the strings are equal
        if len(s1) != len(s2) or len(s1) != len(s3):
            return -1  # Return -1 if the lengths are not equal
        
        operations = 0  # Variable to keep track of the number of operations
        
        # Iterate through each character in the strings
        for i in range(len(s1)):
            # Check if the characters are not equal
            if s1[i] != s2[i] or s1[i] != s3[i]:
                # Increment the number of operations
                operations += 1
        
        return operations
