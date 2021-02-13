class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for item in range(1,len(prices)):
            if(prices[item] > prices[item-1]):
                profit += (prices[item] - prices[item-1])
        return profit
        