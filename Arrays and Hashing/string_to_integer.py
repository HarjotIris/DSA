class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0
        
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        
        return num
    

sol = Solution()
print(sol.myAtoi('042'))
print(sol.myAtoi('-042'))
print(sol.myAtoi('1337c0d3'))
print(sol.myAtoi('0-1'))