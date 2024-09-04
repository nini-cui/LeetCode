#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
import functools
class Solution:
    def largestNumber(self, nums) -> str:
        for i,n in enumerate(nums):
            nums[i]=str(n)
        def comparison(n,m):
            if n+m>m+n:
                return -1
            else:
                return 1
        nums=sorted(nums, key=functools.cmp_to_key(comparison))
        return str(int("".join(nums)))


        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.largestNumber([3,30,34,5,9])