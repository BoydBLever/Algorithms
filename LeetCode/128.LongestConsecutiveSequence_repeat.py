class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Hash Set Creation
        num_set = set(nums)
        max_count = 0
        # 2. Set Iteration: how to determine if a number is the start of a sequence?
        for num in num_set:
            # Check if 'num' is the start of a sequence
            if (num - 1) not in num_set:
                cur_num = num
                cur_count = 1
                # Check if the next number is in the set
                while (cur_num + 1) in num_set:
                    cur_num += 1
                    cur_count += 1
                # Update max_count if this sequence is longer than the recorded max 
                max_count = max(max_count, cur_count)
        return max_count