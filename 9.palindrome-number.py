import math
#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Palindrome:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        iter_num = math.floor(len(str_x) / 2)

        for i in range(iter_num):
            if str_x[i] != str_x[-(i+1)]:
                return False
        
        return True


# @lc code=end
if __name__ == '__main__':
    Palindrome().isPalindrome(121)
    # Palindrome().isPalindrome(1000021)
