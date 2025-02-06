class Solution:
    def reverseWords(self, s: str) -> str:
        res = list(s)
        beg = 0
        for i in range(len(s)):
            if res[i] == " ":
                res[beg:i] = reversed(res[beg:i])
                beg = i+1
        res[beg:] = reversed(res[beg:])
        return "".join(res)
    
sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))