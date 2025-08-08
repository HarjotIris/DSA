class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        if n == 0:
            return [[]]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        result = [[0] * n for _ in range(n)]
        num = 1

        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                result[top][col] = num
                num += 1
            top += 1

            for row in range(top, bottom + 1):
                result[row][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result[bottom][col] = num
                    num += 1
                bottom -= 1

            if top <= bottom:
                for row in range(bottom, top - 1, -1):
                    result[row][left] = num
                    num += 1
                left += 1
        return result