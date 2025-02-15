class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        res = [1]*len(nums)
        left_product = 1
        for i in range(len(nums)):
            res[i] *= left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res
            

        
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))

        