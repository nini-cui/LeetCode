#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List
# @lc code=start
class pascalTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]

        if numRows >= 3:
            res = [[1], [1, 1]]

            for i in range(2, numRows):
                ans = []
                ans.append(1)
                prev_lst = res[i-1]
                for k in range(1, i):
                    ans.append(prev_lst[k-1] + prev_lst[k]) 
                ans.append(1)

                res.append(ans)

        return res               
# @lc code=end
if __name__ == "__main__":
    pascalTriangle = pascalTriangle()
    pascalTriangle.generate(5)