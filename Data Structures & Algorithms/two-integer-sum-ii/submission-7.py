class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #0, 1, 2, 3,  target 5
        #      L  R
        #return [2, 3]

        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return[l + 1, r + 1]
            if total < target:
                l += 1
            else:
                r -= 1

            
        