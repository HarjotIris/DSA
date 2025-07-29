class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]

        for i in range(1, numRows):
            row = [1]
            prev = triangle[-1]
            
            for j in range(1, len(prev)):
                sum = prev[j-1] + prev[j]
                row.append(sum)

            row.append(1)
            triangle.append(row)
        return triangle
    
sol = Solution()
print(sol.generate(5))