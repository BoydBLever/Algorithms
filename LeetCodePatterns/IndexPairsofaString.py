class Solution:
    """
    @param text: A string.
    @param words: A list of strings.
    @return: Index pairs of a string.
    """
    def index_pairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        for word in words:
            start = 0
            while True:
                idx = text.find(word, start)
                if idx == -1:
                    break
                res.append([idx, idx + len(word) - 1])
                start = idx + 1
        res.sort()
        return res
    # Time Complexity: O(n * m), n = len(text), m = len(words)
    # Space Complexity: O(1)