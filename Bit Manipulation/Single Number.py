class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        '''
        nums.sort()
        length = len(nums)
        a = nums[0]

        if length == 1:
            return a

        if a != nums[1]:
            return a

        if nums[-1] != nums[-2]:
            return nums[-1]

        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]

        '''
        result = 0
        for num in nums:
            result ^= num
        return result