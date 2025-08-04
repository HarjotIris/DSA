class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # O(n)
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(current_sum, max_sum)

        return max_sum
       
        '''
        # dp
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum
        '''