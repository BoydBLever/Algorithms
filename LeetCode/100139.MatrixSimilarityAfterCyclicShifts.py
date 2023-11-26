class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # Helper function to perform the cyclic shift
        def cyclic_shift(arr, k):
            k %= len(arr)
            return arr[-k:] + arr[:-k]
        
        # Check each row after performing the cyclic shift
        for i in range(len(mat)):
            shifted = cyclic_shift(mat[i], k if i % 2 == 0 else -k)
            if shifted != mat[i]:  # If shifted row is not equal to the original, return False
                return False
        
        return True  # If all rows are unchanged after the shift, return True