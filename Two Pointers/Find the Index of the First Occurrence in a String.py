class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # lol ---> return haystack.find(needle)

        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return - 1
    
'''
Ask these questions every time:

What is the range of the loop and why?

What does each iteration check?

What happens if it finds a match?

What happens if no match is found?
'''

