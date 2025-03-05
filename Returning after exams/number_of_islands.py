class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        island_counter = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    island_counter += 1
                    dfs(r, c)

        return island_counter


sol = Solution()
print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # 1
print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # 3