#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start

# hi
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in map_dict and map_dict[compliment] != i:
                return [i, map_dict[compliment]]

            map_dict[nums[i]] = i
        

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.twoSum([3, 2, 4], 6)
