class Solution:# optimal solution:
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

sol = Solution()
print(sol.largestRectangleArea([7,1,7,2,2,4])) # 8
print(sol.largestRectangleArea([1,3,7])) # 7
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3])) # 10
print(sol.largestRectangleArea([5])) # 5
print(sol.largestRectangleArea([2, 2]))  # 4
print(sol.largestRectangleArea([5, 4, 3, 2, 1]))  # 9
print(sol.largestRectangleArea([3, 3, 3, 3])) # 12 


'''
class Solution: # my solution:
    # Time Complexity - O(n²)
    # Space Complexity - O(1)
    def largestRectangleArea(self, heights: list[int]) -> int:
        area = 0

        for i, val in enumerate(heights):
            new_area = 0
            stack = []
            stack.append(val)
            width = 1

            if i > 0:
                j = i - 1
                while j >= 0 and heights[j] >= stack[-1]:
                    width += 1
                    j -= 1

            new_area += stack[-1] * width
            width = 0
            j = i + 1

            while j < len(heights) and heights[j] >= stack[-1]:
                width += 1
                j += 1

            new_area += stack.pop() * width
            area = max(area, new_area)

        return area

sol = Solution()
print(sol.largestRectangleArea([7,1,7,2,2,4])) # 8
print(sol.largestRectangleArea([1,3,7])) # 7
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3])) # 10
print(sol.largestRectangleArea([5])) # 5
print(sol.largestRectangleArea([2, 2]))  # 4
print(sol.largestRectangleArea([5, 4, 3, 2, 1]))  # 9
print(sol.largestRectangleArea([3, 3, 3, 3])) # 12   
'''
        