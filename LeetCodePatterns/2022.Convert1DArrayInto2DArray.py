class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Initial check
        if len(original) != m * n:
            return []
        # Construct the 2D array
        # Initialize an empty array which will hold the find 2D array
        # Why iterate m times? Because we need to construct m rows.
        res = []
        # iterate m times for each row
        for i in range(m):
        # extract a slice of length n from original array and append it to the res array, starting from i * n to (i + 1) * n. This slice represents a row in the 2D array.
        # each slice grabs exactly n elements from the original array, corresponding to a single row of the 2D array.
            res.append(original[i * n: (i + 1) * n])
        return res