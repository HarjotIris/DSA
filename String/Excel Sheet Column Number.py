class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        multiplier = 0
        num = 0
        for letter in columnTitle:
            num *= 26
            num += ord(letter) - 64
            multiplier += 1
        return num