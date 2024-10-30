class Solution: # optimal solution
    # Time - O(n), Space - O(1)
    def maxArea(self, heights: list[int]) -> int:
        container = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            container = max(container, area)
            # updating pointers in a way that the pointer at the shorter height moves inward
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            # Since the shorter height limits the container, 
            # keeping one of the pointers at this shorter 
            # height while moving the other pointer doesn’t help; 
            # the area won’t increase because the container’s height 
            # is still limited by this shorter bar.

            # By moving the pointer at the shorter bar inward, 
            # we’re attempting to find a taller bar that might yield a greater area, 
            # as it increases the minimum height of the container.

            '''
            By always moving the pointer at the shorter height inward, 
            this approach efficiently skips combinations that wouldn't yield 
            a larger area, which is what allows it to run in O(n) time. 
            This logic is based on the fact that the area can only increase 
            by either increasing the container's height or width, 
            and since the width decreases as l and r move closer, 
            increasing height becomes the only viable path 
            for a potential area increase.
            '''
        return container

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))



'''
class Solution: # my solution
    # Time - O(n²), Space - O(1)
    def maxArea(self, heights: list[int]) -> int:
        container = 0
        for i in range(len(heights)):
            l, r = i, len(heights)-1
            while l < r:
                dist = abs(l-r) # calculate the distance
                area = min(heights[l], heights[r]) * dist # calculate the area
                container = max(container, area)
                r -= 1                                 
        return container

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))
'''        