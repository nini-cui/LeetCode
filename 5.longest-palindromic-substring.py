#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res = set()

        # for i in range(len(s)-1):
        #     for j in range(i+1, len(s)):
        #         current_str = s[i] + s[i+1:j+1]
        #         if current_str == current_str[::-1]:
        #             res.add(current_str)

        # return max(res, key=len)
        
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str
    
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.longestPalindrome("babad")
