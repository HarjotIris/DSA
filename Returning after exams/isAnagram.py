class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for char in s:
            dict_s[ord(char)-97] = 1 + dict_s.get((ord(char)-97), 0)

        for char in t:
            dict_t[ord(char)-97] = 1 + dict_t.get((ord(char)-97), 0)
        
        if dict_s == dict_t:
            return True
        return False
        
sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
print(sol.isAnagram("jam", "jar"))

'''
Sophisticated solution #1 --
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

        
Sophisticated solution #2 --
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
'''