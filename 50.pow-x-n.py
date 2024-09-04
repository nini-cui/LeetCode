#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        
        if n < 1:
            return False
        
        return self.isPowerOfTwo(n/2)

# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.isPowerOfTwo(3)
    # solution.myPow(2.00000, 6)