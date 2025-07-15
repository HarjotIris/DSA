
class Solution:
    def climbStairs(self, n: int, cache = None) -> int:
        '''
        # memoization
        if cache is None:
            cache = {}
        if n == 0 or n == 1:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.climbStairs(n-1, cache) + self.climbStairs(n-2, cache)
        return cache[n]
        '''
        '''
        # dp - 1st way
        if n <= 1:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        '''
        # dp most optimal solution
        if n <= 1:
            return 1
        a, b = 1, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
sol = Solution()
print(sol.climbStairs(5))
