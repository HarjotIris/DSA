class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0 and carry:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1

        if carry:
            digits.insert(0, carry)
        return digits