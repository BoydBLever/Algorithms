class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        count = 0
        vowels = "aeiou"

        # Helper function to check if a substring is beautiful
        def is_beautiful(sub):
            vowel_count = sum(1 for char in sub if char in vowels)
            consonant_count = len(sub) - vowel_count
            # Check if the product of vowels and consonants is divisible by k
            return vowel_count * consonant_count % k == 0 if vowel_count * consonant_count > 0 else False
        
        # Check all possible substrings
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if is_beautiful(s[i:j]):
                    count += 1
        
        return count