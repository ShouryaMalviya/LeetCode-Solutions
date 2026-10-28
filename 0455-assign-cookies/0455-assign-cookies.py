class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        
        child_ptr = 0
        cookie_ptr = 0
        
        while child_ptr < len(g) and cookie_ptr < len(s):
            # If the current cookie can satisfy the current child
            if s[cookie_ptr] >= g[child_ptr]:
                child_ptr += 1
            # Move to the next cookie in all cases
            cookie_ptr += 1
            
        return child_ptr