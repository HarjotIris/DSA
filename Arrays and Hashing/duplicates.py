class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        new = []
        for _ in nums:
            if _ in new:
                return True
            new.append(_)
        return False
                
sol = Solution()
print(sol.hasDuplicate([1,2,3,3]))