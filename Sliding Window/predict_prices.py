class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit  = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit


sol = Solution()
print(sol.maxProfit([10,1,5,6,7,1])) # 6
print(sol.maxProfit([10,8,7,5,2])) # 0
print(sol.maxProfit([1, 2, 3, 4, 5])) # 4
print(sol.maxProfit([7, 1, 5, 3, 6, 4])) # 5
print(sol.maxProfit([2, 4, 1, 5, 3, 6, 2, 8])) # 7
        
        