#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        mapping = {
            1000: "M",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        for val, char in mapping.items():
            if num // val:
                count = num // val
                res += count * char
                num = num % val
        
        return res
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.intToRoman(3749)
