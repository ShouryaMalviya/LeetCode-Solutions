from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count how many characters have an odd frequency
        odds = sum(count % 2 for count in Counter(s).values())
        
        # If there are odd frequencies, we lose (odds - 1) characters. 
        # If no odd frequencies, we use the whole string.
        return len(s) - odds + 1 if odds > 0 else len(s)