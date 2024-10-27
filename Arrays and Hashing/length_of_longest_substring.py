class Solution: # better solution using sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in res_set:
                res_set.remove(s[l])
                l += 1
            res_set.add(s[r])
            res = max(res, len(res_set))
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring("dvdf"))

'''
class Solution: #my solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_str = ""
        res = 0
        for i in range(len(s)):
            res_str = "" + s[i]
            for j in range(i+1, len(s)):
                if s[j] in res_str:
                    res = max(res, len(res_str))
                    break
                else:
                    res_str += s[j]
            res = max(res, len(res_str))
        return res


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
'''