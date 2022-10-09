#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif len(str(x)) == 1:
            return True
        else:
            int_list = [int(x) for x in str(x)]
            for i in range(int(len(int_list)/2)):
                if (int_list[i] == int_list[len(int_list) - i - 1]):
                    return True
                else:
                    return False


# @lc code=end
if __name__ == '__main__':
    Solution().isPalindrome(1000021)
