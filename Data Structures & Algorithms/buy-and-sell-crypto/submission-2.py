class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        prof = 0
        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l = r
            if prices[r] - prices[l] > prof:
                prof = prices[r] - prices[l]
        return prof
