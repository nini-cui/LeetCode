#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        sequence = set()
        repeated = set()

        for i in range(len(s)-9):
            sub_str = s[i:i+10]
            if sub_str in sequence:
                repeated.add(sub_str)
            else:
                sequence.add(sub_str)

        return repeated

        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
