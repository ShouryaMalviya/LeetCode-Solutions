class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove existing dashes and convert everything to uppercase
        s = s.replace("-", "").upper()
        
        res = []
        count = 0
        
        # Traverse the string from right to left
        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
            count += 1
            
            # After every 'k' characters (and if it's not the end of the string), add a dash
            if count == k and i > 0:
                res.append("-")
                count = 0
                
        # Since we built the string backwards, reverse the result list and join
        return "".join(res[::-1])