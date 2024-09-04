#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def make_combination(idx, combo, total):
            if total == target:
                res.append(combo[:])
                return

            if total > target or idx >= len(candidates):
                return 
            
            combo.append(candidates[idx])
            make_combination(idx, combo, total+candidates[idx])
            combo.pop()
            make_combination(idx+1, combo, total)

            return res

        return make_combination(0, [], 0)
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.combinationSum([2,3,6,7], 7)
