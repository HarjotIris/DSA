class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        stack = []
        result = []

        def backtracking(open_count, closed_count):
            if open_count == closed_count == n:
                result.append("".join(stack))
                return
            
            if open_count < n:
                stack.append("(")
                backtracking(open_count + 1, closed_count)
                stack.pop()

            if closed_count < open_count:
                stack.append(")")
                backtracking(open_count, closed_count + 1)
                stack.pop()
        backtracking(0, 0)
        return result
        

sol = Solution()
print(sol.generateParenthesis(3))