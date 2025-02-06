class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        beg = 0
        end = len(s)-1
        while beg < end:
            s[beg], s[end] = s[end], s[beg]
            beg += 1
            end -= 1
        return s
    
sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))
print(sol.reverseString(["H","a","n","n","a","h"]))