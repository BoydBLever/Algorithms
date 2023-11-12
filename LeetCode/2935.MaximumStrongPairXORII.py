from typing import List

class XorTrieNode:
    def __init__(self):
        self.child = [None, None]
        self.count = 0

class XorTrie:
    def __init__(self):
        self.root = XorTrieNode()

    def insert(self, num):
        node = self.root
        for i in reversed(range(20)):  # Assuming 20 bits for the problem
            bit = (num >> i) & 1
            if not node.child[bit]:
                node.child[bit] = XorTrieNode()
            node = node.child[bit]
            node.count += 1

    def remove(self, num):
        node = self.root
        for i in reversed(range(20)):  # Assuming 20 bits for the problem
            bit = (num >> i) & 1
            if node.child[bit].count == 1:
                node.child[bit] = None
                return
            node = node.child[bit]
            node.count -= 1

    def maxXor(self, num):
        node = self.root
        max_xor = 0
        for i in reversed(range(20)):  # Assuming 20 bits for the problem
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if node.child[toggled_bit] and node.child[toggled_bit].count > 0:
                max_xor |= (1 << i)
                node = node.child[toggled_bit]
            else:
                node = node.child[bit]
        return max_xor

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        trie = XorTrie()
        nums.sort()
        max_xor = 0
        j = 0
        for i, num in enumerate(nums):
            trie.insert(num)
            while j < i and nums[j] * 2 < num:
                trie.remove(nums[j])
                j += 1
            max_xor = max(max_xor, trie.maxXor(num))
        return max_xor

# Example usage:
# sol = Solution()
# result = sol.maximumStrongPairXor([3, 49, 81, 95, 92])
# print(result)  # Expected output: 110
