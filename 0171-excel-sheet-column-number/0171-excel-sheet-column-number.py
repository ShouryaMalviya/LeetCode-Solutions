class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # ord(char) - ord('A') + 1 gets the 1-based index of the letter (A=1, B=2, etc.)
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result