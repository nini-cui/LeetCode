#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = dict()

        for i in s:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
                
        if len(set(s)) != len(set(t)):
            return False
        
        for i in t:
            if i not in res:
                return False
            elif t.count(i) != res[i]:
                return False
            
        return True
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.isAnagram("ab", "a")
