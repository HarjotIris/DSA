class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        HashMap = {}
        for index, value in enumerate(nums):
            HashMap[value] = index
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in HashMap and HashMap[diff] != i:
                return (i, HashMap[diff])
            
sol = Solution()
print(sol.twoSum([3,4,5,6], 7))
print(sol.twoSum([4,5,6], 10))
print(sol.twoSum([5,2,1,1,5], 10))