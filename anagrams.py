class Solution: # Using list functions
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = list(s) #racecar
        arr2 = list(t) #carrace
        for i in arr1:
            if i in arr2: 
                arr2.remove(i)
        if len(arr2) == 0:
            return True       
        return False


sol = Solution()
print(sol.isAnagram("racecar", "carrace"))


"""
without affecting the original strings
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = list(s) #racecar
        arr2 = list(t) #carrace
        result = arr1.copy()
        for i in arr1:
            if i in arr2: 
                result.remove(i)
        if len(result) == 0:
            return True      
        return False



sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
"""


"""
Using HashMaps / Dictionaries
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count1, count2 = {}, {}

        for i in range(len(s)):
            count1[s[i]] = 1 + count1.get(s[i], 0)
            count2[t[i]] = 1 + count2.get(t[i], 0)
        
        for count in count1:
            if count1[count] != count2.get(count, 0):
                return False
        return True

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
"""


"""
Using Counter Data Structure
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
"""


"""
Using Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
"""