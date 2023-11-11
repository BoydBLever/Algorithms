class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Solution 1: Linear Search
        # the for loop will stop at the first letter that is greater than target, return it, if not found, return the first letter.
        for letter in letters:
            # if letter is greater than target, return it immmediately.
            if letter > target:
                return letter
        return letters[0]
# Time complexity: O(N). You might have to check every element in the list once. This occurs when either the target is greater than or equal to all elements in the list, of the target is the very last one in the list.
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
        # the modulation operation is used to handle the case where the target is greater than all elements in the list, in which case the lo will be out of bounds. When the target letter is greater than all letters in the array, the lo pointer will eventually be incremented to len(letters) - one past the end of the array - by the end of the while loop. In this case, we need to wrap around the array by using the modulus operator.
        # If lo equals len(letters), it means the target letter is greater than all the letters in the array. In this case, you need to wrap around to the beginning of the array, and the modulus operator (%) is used for this purpose.
        return letters[lo % len(letters)]