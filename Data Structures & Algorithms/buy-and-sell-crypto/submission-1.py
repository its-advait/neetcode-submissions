class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        prof = 0
        for r in range(len(prices)):
            while r > l and prices[r] < prices[l]:
                l += 1
            if prof < prices[r] - prices[l]:
                prof = prices[r] - prices[l]
        return prof