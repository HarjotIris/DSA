class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        area = 0
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                area += max_l - height[l] # if it's the same as height[l] then nothing gets added, otherwise we get the area

            else: # this works only if max_r >= max_l, so we can cover the value where l = r and we do not have to worry about overlapping pointers
                r -= 1
                max_r = max(max_r, height[r])
                area += max_r - height[r] 
        return area

                
sol = Solution()
print(sol.trap([0,2,0,3,1,0,1,3,2,1]))
        