class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        total = 0
        carry = 0
        result = []
        
        # a = '1010' , b = '1011'
        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1
            
            result_bit = total % 2
            carry = total // 2
            result.append(str(result_bit))

        
        return ''.join(reversed(result))
            

sol = Solution()
print(sol.addBinary("11", "1"))