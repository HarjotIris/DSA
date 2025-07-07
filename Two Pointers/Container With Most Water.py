class Solution:
    def maxArea(self, height: list[int]) -> int:
        # solved this medium first try let's go
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            minimum_height = min(height[left], height[right])
            area = max(area, (right - left)* minimum_height)

            if minimum_height == height[left]:
                left += 1
            else: 
                right -= 1
        return area
    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))