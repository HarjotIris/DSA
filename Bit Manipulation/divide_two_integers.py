class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31 

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = -1 if (divisor < 0) ^ (dividend < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            q += multiple

        q *= sign

        return max(min(q, INT_MAX), INT_MIN)