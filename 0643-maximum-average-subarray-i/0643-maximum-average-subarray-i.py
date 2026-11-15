class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Step 1: Calculate the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Step 2: Slide the window from index k to the end of the array
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
                
        # Step 3: Return the maximum average
        return max_sum / k