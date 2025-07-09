class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        nums.sort()
        length = len(nums)
        closest_sum = float('inf')

        for i in range(length - 2):
            left, right = i + 1, length - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
    
sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))

