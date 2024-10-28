class Solution: # solution using a formula for jumps
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):  # Handle edge cases
            return s
        
        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1 and
                    i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))


'''
class Solution: # my solution
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):  # Handle edge cases
            return s
        arr = [[""]*len(s) for _ in range(numRows)]
        row_mover, col_mover, char_count = 0, 0, 0

        while char_count < len(s):
            while row_mover < numRows and char_count < len(s):
                arr[row_mover][col_mover] = s[char_count]
                char_count += 1
                row_mover += 1
            
            col_mover += 1
            row_mover -= 2

            while row_mover > 0 and char_count < len(s):
                arr[row_mover][col_mover] = s[char_count]
                char_count += 1
                row_mover -= 1
                col_mover += 1

        res = ""
            
        for row in arr:
            for col in row:
                if col: # skipping empty strings and zeros
                    res += col

        return res


sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
'''