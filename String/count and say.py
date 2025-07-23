class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        current = '1'

        for _ in range(n-1):
            next_term = ''

            i = 0

            while i < len(current):
                count = 1

                while i + 1 < len(current) and current[i] == current[i+1]:
                    count += 1
                    i += 1

                next_term += str(count) + current[i]
                i += 1

            current = next_term

        return current