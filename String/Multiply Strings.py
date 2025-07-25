class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' and num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit_1 = int(num1[i])
                digit_2 = int(num2[j])
                result[i+j] += digit_1 * digit_2

        for k in range(len(result)):
            carry = result[k] // 10
            result[k] = result[k] % 10
            if k + 1 < len(result):
                result[k+1] += carry

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(map(str, result[::-1]))