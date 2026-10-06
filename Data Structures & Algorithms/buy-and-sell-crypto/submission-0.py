class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        best_sell = 0

        for price in prices:
            best_buy = min(best_buy, price)
            best_sell = max(best_sell, price - best_buy)
        
        return best_sell
