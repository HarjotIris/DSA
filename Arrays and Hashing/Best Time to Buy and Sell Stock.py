class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        profit = 0
        length = len(prices)
        i = 0
        for i in range(length - 1) :
            if prices[i] > prices[i + 1]:
                continue
            for j in range(i + 1, length):
                if prices[j] <= prices[i]:
                    continue
                profit = max(profit, (prices[j] - prices[i]))
        return profit
        '''

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit