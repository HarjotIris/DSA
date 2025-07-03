class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev = 0
        x = abs(x)

        while x!=0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign

        if rev > 2**31 - 1 or rev < -2 ** 31:
            return 0
        
        return rev
    
sol = Solution()
print(sol.reverse(123))