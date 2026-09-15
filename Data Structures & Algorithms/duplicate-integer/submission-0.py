class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        index = len(nums)

        for i in range(index):
            for j in range(0, index):
                if nums[i] == nums[j] and j != i:
                    return True
        return False