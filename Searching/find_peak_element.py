class Solution: # O(log n) time
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
print(sol.findPeakElement([1,2,3,1]))
print(sol.findPeakElement([1,2,1,3,5,6,4]))
        
'''
class Solution: # O(n) time
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, 1

        while right < len(nums):
            if nums[right] > nums[left]:
                left += 1
                right +=1

            else:
                return left
        return None

sol = Solution()
print(sol.findPeakElement([1,2,3,1]))
print(sol.findPeakElement([1,2,1,3,5,6,4]))
'''     