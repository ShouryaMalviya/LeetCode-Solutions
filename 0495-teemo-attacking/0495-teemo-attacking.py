class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
            
        total_time = 0
        for i in range(len(timeSeries) - 1):
            # Add the time until the next attack, capped at 'duration'
            total_time += min(timeSeries[i+1] - timeSeries[i], duration)
            
        # The last attack always lasts for the full duration
        total_time += duration
        
        return total_time