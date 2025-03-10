class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def permute(nums, path = []):
            if not nums:
                result.append(path)
                return
            
            for i in range(len(nums)):
                permute(nums[:i] + nums[i+1:], path + [nums[i]])

        permute(nums, [])
        return result
    
sol = Solution()
print(sol.permute([1,2,3]))
print(sol.permute([1,2]))
print(sol.permute([]))