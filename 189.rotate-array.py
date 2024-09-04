#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums, k: int) -> None:
        k = k % len(nums)

        for i in range(k):

            prev = nums[-1]
            for j in range(len(nums)):
                temp = nums[j]
                nums[j] = prev
                prev = temp

        return nums[i]

        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.rotate([1,2,3,4,5], 8)
