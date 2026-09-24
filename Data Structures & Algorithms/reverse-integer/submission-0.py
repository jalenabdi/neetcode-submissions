class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        remainder = 0
        negative = x < 0
        x = abs(x)
    
        while x > 0:
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x = x // 10
        

        if not (-2**31 <= reverse <= 2**31 - 1):
            return 0

        return -reverse if negative else reverse

        