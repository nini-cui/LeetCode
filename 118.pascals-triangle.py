#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List
# @lc code=start
class pascalTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result

        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)

        return result

        # if numRows == 0:
        #     return []
        # elif numRows == 1:
        #     return [[1]]
        
        # prevVal = self.generate(numRows-1)
        # currentVal = [1] * numRows

        # for i in range(1, numRows-1):
        #     currentVal[i] = prevVal[-1][i] + prevVal[-1][i-1]

        # prevVal.append(currentVal)

        # return prevVal


        # res = []
        # for i in range(1, numRows+1):
        #     current_arr = i * [1]
        #     if (len(current_arr) == 1) or (len(current_arr) == 2):
        #         res.append(current_arr)
        #     else:
        #         prev_arr = res[i-2]
        #         for k in range(1, i-1):
        #             current_arr[k] = prev_arr[k] + prev_arr[k-1]
        #         res.append(current_arr)

        # return res                    
# @lc code=end
if __name__ == "__main__":
    pascalTriangle = pascalTriangle()
    pascalTriangle.generate(5)