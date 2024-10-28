class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = ""
        res = ""
        for i in range(len(s)):
            # checking for odd length palindromes
            l = i
            r = i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                l -= 1
                r += 1
            temp = s[l+1:r] # reason because the loop terminated when the values at the pointers became false, so right now the pointers are at +1 index from when they were palindrome, and we only need the substring of the palindrome, so we slice from l+1 to r-1
            if len(temp)>len(res):
                res = temp
            # checking for even length palindromes
            l = i
            r = i + 1
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                l -= 1
                r += 1
            temp = s[l+1:r]
            if len(temp)>len(res):
                res = temp
        return res

sol = Solution()
print(sol.longestPalindrome("anjdbbdkonj"))
