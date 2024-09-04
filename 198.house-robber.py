#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        res = []
        for i in range(len(nums)-2):
            level_total = 0
            level_total += nums[i]
            
            for j in range(i+2, len(nums), 2):
                level_total += nums[j]

            res.append(level_total)

        return max(res)
    
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.rob([1, 3, 1])
