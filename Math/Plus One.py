class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        else:

            carry = 1
            i = len(digits) - 1

            while i >= 0:
                sum = digits[i] + carry
                digits[i] = sum % 10
                carry = sum // 10
                i -= 1

                if carry == 0:
                    break

            if carry:
                digits.insert(0, carry)

        return digits
    

sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([4,3,2,1]))
print(sol.plusOne([9]))