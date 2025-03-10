from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)

        def track_paths(row, col):
            if row == m-1 and col == n-1:
                return 1
            elif row >= m or col >= n:
                return 0
            
            return track_paths(row + 1, col) + track_paths(row, col + 1)
        return track_paths(0, 0)
    
sol = Solution()
print(sol.uniquePaths(3, 7))
    

