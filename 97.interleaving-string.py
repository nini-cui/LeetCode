#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
                    
        return dp[0][0]



        # m, n = len(s1), len(s2)

        # if m + n != len(s3):
        #     return False
        
        # dp = [[False] * (n + 1) for _ in range(m + 1)]

        # dp[0][0] = True

        # for i in range(1, m + 1):
        #     dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # for j in range(1, n + 1):
        #     dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         choose_s1, choose_s2 = False, False
        #         if s1[i - 1] == s3[i + j - 1]:
        #             choose_s1 = dp[i - 1][j]
        #         if s2[j - 1] == s3[i + j - 1]:
        #             choose_s2 = dp[i][j - 1]
        #         dp[i][j] = choose_s1 or choose_s2

        # return dp[m][n]

        # dp = {}
        # if len(s1) + len(s2) != len(s3):
        #     return False
        
        # def dfs(i, j):
        #     if i == len(s1) and j == len(s2):
        #         return True
        #     if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
        #         return True
        #     if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j+1):
        #         return True
            
        #     dp[(i, j)] = False
        #     return False

        # return dfs(0, 0)
        
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.isInterleave("aabcc", "dbbca", "aadbbcbcac")
