class Solution:# with stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0]* len(temperatures)
        stack = [] # pair : [temp, index]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = index - stack_i
            stack.append([temp, index])
        return res

sol = Solution()
print(sol.dailyTemperatures([30,38,30,36,35,40,28]))
        
'''
class Solution: # without stack
    # Time Complexity: O(n²)
    # Space Complexity: O(n)
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = []
        for i, val in enumerate(temperatures):
            count  = 0
            foundWarmer = False

            for k in range(i+1, len(temperatures)-1):
                count += 1
                if temperatures[k] > val:
                    res.append(count)
                    foundWarmer = True
                    break
            if not foundWarmer:
                res.append(0)

        return res

sol = Solution()
print(sol.dailyTemperatures([30,38,30,36,35,40,28]))
'''
        