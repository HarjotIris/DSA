import collections
class Solution: # Time Complexity - O(1), Space Complexity - O(1)
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqaures = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                      board[r][c] in cols[c] or 
                      board[r][c] in sqaures[(r//3, c//3)]):
                      return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqaures[(r//3, c//3)].add(board[r][c])
        return True
sol = Solution()
print(sol.isValidSudoku([
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
        

'''
class Solution: # Time Complexity - O(1), Space Complexity - O(1)
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row, col = 9,9
        # checks dups in rows
        for r in board:
            num = []
            for _ in r:
                if _ == ".":
                    continue
                elif _ in num:
                    return False
                else:
                    num.append(_)
        # checks duplicates in columns
        for c in range(col):
            num = []
            for r in board:
                if r[c] == ".":
                    continue
                elif r[c] in num:
                    return False
                else:
                    num.append(r[c])

        for i in range(0, row, 3):
            for j in range(0, col, 3):
                num = []
                for k in range(3):
                    for l in range(3):
                        if board[k+i][l+j] == ".":
                            continue
                        elif board[k+i][l+j] in num:
                            return False
                        else:
                            num.append(board[k+i][l+j])
        return True
    

# Testing the solution
sol = Solution()
print(sol.isValidSudoku([
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
'''
