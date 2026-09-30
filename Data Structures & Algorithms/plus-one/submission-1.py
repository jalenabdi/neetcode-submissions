class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        arr = []

        for i in range(len(digits)):
            res = res*10 + digits[i]
        res += 1

        res = str(res)
        n = 0

        while n < len(res):
            arr.append(int(res[n]))
            n += 1

        return arr