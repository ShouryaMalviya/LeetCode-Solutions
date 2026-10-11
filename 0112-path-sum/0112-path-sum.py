# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base Case: Agar node exist nahi karta (jaise Example 3 mein empty tree hai)
        if not root:
            return False
        
        # Agar yeh ek leaf node hai (iske left aur right children nahi hain)
        # toh check karein ki kya bacha hua targetSum is node ki value ke barabar hai
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively left aur right branches mein check karein
        # Aur current targetSum mein se current node ki value ko minus karte jayein
        remaining_sum = targetSum - root.val
        
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))