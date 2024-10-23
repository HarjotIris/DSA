from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1
            
            result[tuple(count)].append(s)
        
        return result.values()
            
                
sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(sol.groupAnagrams(["x"]))
print(sol.groupAnagrams([""]))