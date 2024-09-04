#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique_vals = list(set(nums))
        for i in unique_vals:
            if nums.count(i) > len(nums)/2:
                return i
            
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.majorityElement([3,2,3])
