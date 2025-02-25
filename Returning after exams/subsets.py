class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]
        return result

sol = Solution()
print(sol.subsets([1,2,3]))
print(sol.subsets([0]))
print(sol.subsets([]))
        