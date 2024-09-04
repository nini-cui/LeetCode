#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:

    def wordBreak(self, s, wordDict):

        # n = len(s)
        # word_set = set(wordDict)

        # dp = [False] * (n + 1)

        # dp[0] = True

        # for i in range(1, n + 1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in word_set:
        #             dp[i] = True
        #             break

        # return dp[n]
    
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    break
                    
        return dp[-1]
    
        
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"])
