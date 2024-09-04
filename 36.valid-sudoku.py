#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board) -> bool:
        def is_row_valid(board):
            for row in board:
                if not is_unit_valid(row):
                    return False
                
            return True
            
        def is_col_valid(board):
            for col in zip(*board):
                if not is_unit_valid(col):
                    return False
            return True
            
        def is_grid_valid(board):
            for i in range(0, len(board), 3):
                for j in range(0, len(board), 3):
                    square_board = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                    if not is_unit_valid(square_board):
                        return False
            return True

        def is_unit_valid(row):
            vals = [val for val in row if val != '.']
            return len(set(vals)) == len(vals)
        
        # return (is_row_valid(board) and is_col_valid(board) and is_grid_valid(board))
        return (is_row_valid(board) and is_col_valid(board) and is_grid_valid(board))
    
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.isValidSudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]])
