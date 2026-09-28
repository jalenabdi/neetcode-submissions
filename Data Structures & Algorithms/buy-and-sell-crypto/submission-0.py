class Solution(object):
    def maxProfit(self, prices):
        #res = 5
        #7, 1, 5, 3, 6, 4
        #   L  R
        #res=max(r-l,res)
        l = 0
        r = 1
        res = 0

        while r < len(prices):
            temp = prices[r] - prices[l]
            if temp <= 0:
                l = r
                r += 1
            else:
               res = max(prices[r]-prices[l],res)
               r += 1
        return res