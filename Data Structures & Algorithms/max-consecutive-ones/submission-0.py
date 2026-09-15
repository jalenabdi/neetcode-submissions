class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr = []
        consec = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                consec += 1
            else:
               arr.append(consec)
               consec = 0 
        arr.append(consec)
        maxnum = max(arr)
        return maxnum