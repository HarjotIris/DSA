class Solution: # optimal stack solution
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            # if c is an opening bracket
            if c not in Map:
                stack.append(c)
                continue
            # if c is a closing bracket
            # "not stack" checks if the stack is empty
            # if it is empty then we return False
            # and we check whether the current closing bracket
            # matches the corresponding opening bracket
            # as the last value in the stack
            if not stack or stack[-1] != Map[c]:
                return False
            # If the current closing bracket has a matching opening bracket 
            # on the stack, we remove that opening bracket from the stack.
            stack.pop()

        return not stack

sol = Solution()
print(sol.isValid("([{}])"))
print(sol.isValid("[]"))
print(sol.isValid("(("))
print(sol.isValid("()[]{}"))

'''
class Solution: # my solution
    def isValid(self, s: str) -> bool:
        res = []
        x = []
        if 0 <= len(s) <= 1:
            return False
        for i in range(len(s)-1, -1, -1):
            if s[i] == ")" or s[i] == "}" or s[i] == "]":
                res.append(s[i])

            elif s[i] == "(":
                if res:
                    if res[-1] == ")":
                        x.append(res.pop())

            elif s[i] == "{":
                if res:
                    if res[-1] == "}":
                        x.append(res.pop())

            elif s[i] == "[":
                if res:
                    if res[-1] == "]":
                        x.append(res.pop())
            else:
                continue

        if len(res) == 0 and len(x) == len(s)/2:
            return True
        return False


sol = Solution()
print(sol.isValid("([{}])"))
print(sol.isValid("[]"))
print(sol.isValid("(("))
print(sol.isValid("()[]{}"))
'''
