#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

# @lc code=start
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        target = {}
        res = []
        for word2 in words2:
            # get the count of each letter in a word
            letter_mapping = {}
            for letter in word2:
                if letter not in letter_mapping:
                    letter_mapping[letter] = 1
                else:
                    letter_mapping[letter] +=1

            for letter, count in letter_mapping.items():
                if letter in target:
                    target[letter] = max(target[letter], count)
                else:
                    target[letter] = count

        for word in words1:
            append = True
            for letter, count in target.items():
                if word.count(letter) < count:
                    append = False
                    break
            
            if append:
                res.append(word)

        return res

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"])
