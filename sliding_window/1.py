class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit


A = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(A.maxProfit(prices))
