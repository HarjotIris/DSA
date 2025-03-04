class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set_nums1 = set(nums1)
        result = {num for num in nums2 if num in set_nums1}

        return list(result)


sol = Solution()
print(sol.intersection([1,2,2,1], [2, 2]))
print(sol.intersection([4,9,5], [9,4,9,8,4]))
