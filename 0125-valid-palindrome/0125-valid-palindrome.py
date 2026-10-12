class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_s =[char.lower() for char in s if char.isalnum()]

        return cleaned_s == cleaned_s[::-1]
        