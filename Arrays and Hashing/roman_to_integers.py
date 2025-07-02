class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'M':1000,
            'C':100,
            'X':10,
            'D':500,
            'L':50,
            'V':5,
            'I':1
        }
        num = 0
        length = len(s)
        temp = roman_map[s[length-1]]
        for i in range(length-1, -1, -1):
            temp_i = roman_map[s[i]]

            if temp_i < temp:
                num -= temp_i
            else:
                num += temp_i

            temp = temp_i    
        return num
    
sol = Solution()
print(sol.romanToInt("XLVII"))

            
