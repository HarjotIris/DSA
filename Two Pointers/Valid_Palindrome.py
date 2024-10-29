class Solution: # two pointers solution
    # time - O(n), space - O(1)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # to skip the character which is not alphanumeric and to make sure left pointer is in bounds still
            while not self.check_alnum(s[l]) and l < r:
                l += 1
            while not self.check_alnum(s[r]) and r > l:
                r -= 1           

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True
    # function for checking whether a character is alphanumeric or not
    def check_alnum(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))


'''
class Solution: # better solution
    # time - O(n), space - O(n)
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        return new_s == new_s[::-1]

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))
'''

'''
class Solution: # my solution
    # time - O(n), space - O(n)
    def isPalindrome(self, s: str) -> bool:
        res = ""
        new_s = ""
        # creating a new string
        for char in s:
            if char.isalnum():
                new_s += char
        new_s = new_s.lower()
        # storing the reverse string
        for i in range(len(new_s)-1, -1, -1):
                res += new_s[i]

        for i in range(len(new_s)): 
            if new_s[i] != res[i]:
                    return False                    
                
        return True

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))
'''
         