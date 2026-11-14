class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Double the string and remove the first and last characters
        doubled = (s + s)[1:-1]
        # If s is in the modified string, it can be formed by a repeated substring
        return s in doubled