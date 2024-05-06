#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
from typing import List
# @lc code=start
class pascalsTriII:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]*(rowIndex + 1)
        for i in range(2,rowIndex+1):
            for j in range(i-1,0,-1):
                pascal[j] += pascal[j-1]
        return pascal
        # res = []

        # for i in range(rowIndex+1):
        #     cur_arr = [1] * (i+1)

        #     if (i == 0) or (i == 1):
        #         res.append(cur_arr)
        #         continue

        #     for k in range(1, (len(cur_arr)-1)):
        #         cur_arr[k] = res[i-1][k-1] + res[i-1][k]

        #     res.append(cur_arr)
        
        # return res[i]
        
# @lc code=end
if __name__ == "__main__":
    pascalsTriII = pascalsTriII()
    pascalsTriII.getRow(3)