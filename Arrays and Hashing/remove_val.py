class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
    
sol = Solution()
print(sol.removeElement([3,2,2,3],3))
        