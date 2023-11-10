class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Solution 1: Linear Search
        # the for loop will stop at the first letter that is greater than target, return it, if not found, return the first letter.
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
# Time complexity: O(N)
# Space complexity: O(1)
# Binary Search
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = 0, len(letters) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return letters[lo % len(letters)]