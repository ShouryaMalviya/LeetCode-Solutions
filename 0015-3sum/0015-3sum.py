class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # Optimization: If the smallest number is greater than 0, 
            # no three numbers can sum to 0.
            if nums[i] > 0:
                break
            
            # Skip duplicate elements for the first position to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            # Two pointers approach to find the remaining two numbers
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # Need a larger sum, move the left pointer right
                    left += 1
                elif total > 0:
                    # Need a smaller sum, move the right pointer left
                    right -= 1
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second and third positions
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res