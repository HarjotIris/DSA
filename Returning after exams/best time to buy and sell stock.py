class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for price in prices:
            minimum = min(minimum, price)
            maximum = max(maximum, price - minimum)

        return maximum
    
sol = Solution()

print(sol.maxProfit([10,1,5,6,7,1]))
print(sol.maxProfit([10,8,7,5,2]))