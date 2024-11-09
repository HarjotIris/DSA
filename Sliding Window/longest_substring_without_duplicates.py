class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0
        char_set = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length

sol = Solution()
print(sol.lengthOfLongestSubstring("zxyzxyz")) # 3
print(sol.lengthOfLongestSubstring("abcdef")) # 6
print(sol.lengthOfLongestSubstring("aaaaa")) # 1
print(sol.lengthOfLongestSubstring("!@#$%^&*()")) # 10
print(sol.lengthOfLongestSubstring("a b c a b ")) # 3
                