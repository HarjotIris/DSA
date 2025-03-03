class Solution: # Using the XOR bit manipulation method
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s + t:
            result ^= ord(char)
        # same letters having the same ASCII value will cancel each other out in a XOR operation leaving behind the extra letter's ASCII value which we can convert back into a character using the chr function
        return chr(result)
