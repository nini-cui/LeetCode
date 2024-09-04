#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        q = deque()
        level = 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, level))

        while q:
            i, j, level = q.popleft()

            if 0<= i < len(grid) and 0<= j+1 < len(grid[0]) and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                q.append((i, j+1, level+1))

            if 0 <= i < len(grid) and 0<= j-1 < len(grid[0]) and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                q.append((i, j-1, level+1))

            if 0 <= i-1 < len(grid) and 0<= j < len(grid[0]) and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                q.append((i-1, j, level+1))

            if 0 <= i+1 < len(grid) and 0<= j < len(grid[0]) and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                q.append((i+1, j, level+1))
        
        if any(1 in row for row in grid):
            return -1
        else:
            return level
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
