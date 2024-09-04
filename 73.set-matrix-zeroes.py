#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
		
        first_row_has_zero = False
        first_col_has_zero = False
        
        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
    
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        
        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
        # res = []
        # rows = len(matrix)
        # cols = len(matrix[0])

        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             res.append((i, j))

        # for i in res:
        #     row_num = i[0]
        #     col_num = i[1]
        #     # one rows
        #     for j in range(cols):
        #         matrix[row_num][j] = 0

        #     # one col 
        #     for row in range(rows):
        #         matrix[row][col_num] = 0
            
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
