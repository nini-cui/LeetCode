#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur_res, cur_len = [], [], 0

        for word in words:
            if len(word) + cur_len + len(cur_res) > maxWidth:
                size = max(1, len(cur_len)-1)
                for i in range(maxWidth - cur_len):
                    idx = i % size
                    # O(maxWidth - cur_len)
                    cur_res[idx] += " "

                res.append("".join(cur_res))
                cur_res, cur_len = [], 0

            # O(maxWidth)
            cur_res.append(word)
            cur_len += len(word)

        if cur_res:
            res.append(" ".join(cur_res).ljust(16))

        return res
            
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
