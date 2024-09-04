#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str):
        res = []
        # if len(digits) == 0:
        #     return None

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return 
            
            for c in mapping[digits[i]]:
                backtrack(i+1, curStr + c)

        if digits:
            backtrack(0, "")
        
        return res


        # backtracking solution 1
        # res = []
        # def backtrack(combination, next_digits):
        #     if not next_digits:
        #         res.append(combination)
        #         return
            
        #     for letter in mapping[next_digits[0]]:
        #         backtrack(combination + letter, next_digits[1:])
        
        # backtrack("", digits)
        # return res
        
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.letterCombinations("23")
