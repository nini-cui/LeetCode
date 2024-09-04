#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List
class Solution:
    # def partition(self, s: str) -> List[List[str]]:

    #     result = []
    #     lenS = len(s)

    #     def explore(index, curr):
    #         if index >= lenS:
    #             result.append(curr.copy())

    #         for i in range(index, lenS):
    #             subStr = s[index:i + 1]
    #             if subStr == subStr[::-1]:
    #                 curr.append(subStr)
    #                 explore(i + 1, curr)
    #                 curr.pop()

    #     explore(0, [])
    #     return result

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(res, [], s)
        return res
    
    def helper(self, res, curr, s):
        if s == "":
            res.append(curr)
        
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):
                self.helper(res, curr + [s[:i + 1]], s[i + 1:])
    
    def isPalindrome(self, s):
        return s == s[::-1]
            
    # def partition(self, s: str) -> List[List[str]]:
    #     if not s: return [[]]
    #     ans = []
    #     for i in range(1, len(s) + 1):
    #         if s[:i] == s[:i][::-1]:  # prefix is a palindrome
    #             for suf in self.partition(s[i:]):  # process suffix recursively
    #                 ans.append([s[:i]] + suf)
    #     return ans

        
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.partition("aab")
