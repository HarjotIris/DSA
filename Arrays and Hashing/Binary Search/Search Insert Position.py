class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
            
        return low
        '''

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return low
    
sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 7))  # Output: 4
print(sol.searchInsert([1, 3, 5, 6], 0))  # Output: 0
print(sol.searchInsert([1, 3, 5, 6], 5))  # Output: 2