class Solution
    def uniquePathsWithObstacles(self, obstacleGrid List[List[int]]) - int
        ''' backtracking
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1
            return 0
        def backtrack(i, j)
            if i = m or j = n
                return 0

            if obstacleGrid[i][j] == 1
                return 0

            if i == m - 1 and j == n - 1
                return 1

            right_path = backtrack(i, j + 1)
            down_path = backtrack(i + 1, j)

            return right_path + down_path
        
        return backtrack(0, 0)
        '''

        # dp
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1
            return 0

        obstacleGrid[0][0] = 1

        for j in range(1, n)
            if obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1
                obstacleGrid[0][j] = 1
            else
                obstacleGrid[0][j] = 0

        
        for i in range(1, m)
            if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1
                obstacleGrid[i][0] = 1
            else
                obstacleGrid[i][0] = 0

        for i in range(1, m)
            for j in range(1, n)
                if obstacleGrid[i][j] == 0
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else
                    obstacleGrid[i][j] = 0

        return obstacleGrid[m-1][n-1]