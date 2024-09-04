#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return strs

        res = []
        mapping = defaultdict(list)

        for i in strs:
            mapping["".join(sorted(i))].append(i)

        for _, val in mapping.items():
            res.append(val)

        return res
        
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.groupAnagrams([""])
