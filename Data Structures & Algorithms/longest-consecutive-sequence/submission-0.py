class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() 
        
        if not nums:
            return 0
            
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                current_streak += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
    
        return max(longest_streak, current_streak)
