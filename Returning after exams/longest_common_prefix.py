class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:    
        if not strs:
            return ""

        s = strs[0]
        count = len(s)
        for st in strs[1:]:
            new_count = 0
            
            for i in range(min(count, len(st))):
                if s[i] == st[i]:
                    new_count += 1
                else:
                    break
            if new_count == 0:
                    return ""
            count = new_count
        
        return s[:count]
                           
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
        