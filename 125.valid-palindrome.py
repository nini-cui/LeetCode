#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import re
import math
# @lc code=start
class isPalindrome:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        # cleaned_str = re.sub(r'\W+', '', lower_s)
        cleaned_str = re.compile('[^a-zA-Z0-9]').sub('', lower_s)

        split_s = math.floor(len(cleaned_str)/2)

        for i in range(split_s):
            if cleaned_str[i] == cleaned_str[-(i+1)]:
                continue
            else:
                return False
        # s[::-1]
        return True

# @lc code=end
if __name__ == "__main__":
    isPalindrome = isPalindrome()
    isPalindrome.isPalindrome("0P")
